###############################################################################
#                                                                             #
#    This program is free software: you can redistribute it and/or modify     #
#    it under the terms of the GNU General Public License as published by     #
#    the Free Software Foundation, either version 3 of the License, or        #
#    (at your option) any later version.                                      #
#                                                                             #
#    This program is distributed in the hope that it will be useful,          #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of           #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the            #
#    GNU General Public License for more details.                             #
#                                                                             #
#    You should have received a copy of the GNU General Public License        #
#    along with this program. If not, see <http://www.gnu.org/licenses/>.     #
#                                                                             #
###############################################################################

from minION.IO_processor import get_barcode_dict, get_template_sequence
import subprocess
import pysam
import os
from collections import Counter
from pathlib import Path
import pandas as pd
import re
import itertools
import numpy as np
from tqdm import tqdm
from scipy.stats import binomtest, combine_pvalues
from statsmodels.stats.multitest import multipletests

'''
Script for variant calling

The variant caller starts from demultiplexed fastq files. 

1) Before variant calling, check in the demultiplexed folder if the alignment file exists. If not, return the user that the sequences were not demultiplexed
2) If the files exist, create MSA using minimap2
3) Call variant with soft alignment

'''


def check_demultiplexing(demultiplex_folder: Path, reverse_prefix="RB", forward_prefix="NB", verbose=True):
    """
    Check if the demultiplexing was done correctly. If not, return the user that the sequences were not demultiplexed.

    Args:
        - demultiplex_folder: Path to the folder containing the demultiplexed fastq files
        - verbose: If True, print the name of each parent folder and the count of child folders

    Return:
        - Tuple: Number of parent folders and child folders
    """
    demultiplex_path = Path(demultiplex_folder)
    parent_folder_count = 0
    child_folder_count = 0

    for child in demultiplex_path.iterdir():
        if child.is_dir() and (child.name.startswith(reverse_prefix) or child.name.startswith(forward_prefix)):
            parent_folder_count += 1
            child_folder_count += len(list(child.iterdir()))
            if verbose:
                print(f"Parent folder '{child.name}' contains {len(list(child.iterdir()))} folders.")

    return parent_folder_count, child_folder_count


class VariantCaller:
    """
    Variant caller class.

    """

    def __init__(self, experiment_folder: Path,
                 reference_path: Path,
                 barcodes=True,
                 demultiplex_folder_name="demultiplex",
                 front_barcode_prefix="NB", reverse_barcode_prefix="RB", rowwise=False,
                 padding_start: int = 0, padding_end: int = 0) -> None:
        self.reference_path = reference_path
        self.reference = get_template_sequence(reference_path)
        self.experiment_folder = experiment_folder
        self.ref_name = self._get_ref_name()
        self.padding_start = padding_start
        self.padding_end = padding_end
        self.alignment_name = "alignment_minimap.bam"

        if barcodes:
            self.demultiplex_folder = Path(os.path.join(experiment_folder, demultiplex_folder_name))
            self.barcode_dict = get_barcode_dict(self.demultiplex_folder, front_prefix=front_barcode_prefix,
                                                 reverse_prefix=reverse_barcode_prefix)
            self.variant_df = self._get_sample_name()
            self.variant_df = self._rename_barcodes(rowwise=rowwise, merge=True)
            self.variant_df = self._apply_alignment_count()

    def _get_sample_name(self):
        variant_df = {"Parent": [], "Child": [], "Path": []}

        for _, barcode_dict in self.barcode_dict.items():
            for barcode_path in barcode_dict:
                child = os.path.basename(barcode_path)
                parent = os.path.basename(os.path.dirname(barcode_path))

                variant_df["Parent"].append(parent)
                variant_df["Child"].append(child)
                variant_df["Path"].append(Path(barcode_path))

        return pd.DataFrame(variant_df)

    def _rename_barcodes(self, rowwise=False, parent_name="Plate", child_name="Well", merge=True):

        df = self.variant_df

        if rowwise:
            df = df.rename(columns={'Parent': "Row", 'Child': child_name})
            df["Well"] = df["Well"].apply(self._barcode_to_well)
            df["Plate"] = df['Plate'].str.extract('(\d+)').astype(int)

        else:
            df = df.rename(columns={'Parent': parent_name, 'Child': child_name})
            df["Plate"] = df['Plate'].str.extract('(\d+)').astype(int)
            df["Well"] = df["Well"].apply(self._barcode_to_well)

            # Get Plate Numbers
            plate_numbers = df[parent_name].unique()
            plate_numbers.sort()

            if merge:
                template_df = get_template_df(plate_numbers, self.barcode_dict, rowwise=rowwise)
                df = pd.merge(template_df, df, on=[parent_name, child_name], how="left")

        return df

    @staticmethod
    def _barcode_to_well(barcode):
        match = re.search(r'\d+', barcode)
        if match:
            number = int(match.group())
            rows = 'ABCDEFGH'
            row = rows[(number - 1) // 12]
            col = (number - 1) % 12 + 1
            return f"{row}{col}"
        else:
            return "NA"

    def _align_sequences(self, output_dir: Path, scores: list = [4, 2, 10], fastq_prefix="demultiplexed",
                         site_saturation: bool = False, alignment_name: str = "alignment_minimap") -> None:
        """
        Aligns sequences using minimap2, converts to BAM, sorts and indexes the BAM file.

        Args:
            - ref (Path): Path to the reference file.
            - output_dir (str or Path): Directory to store output files.
            - scores (list, optional): List of match, mismatch and gap opening scores. Defaults to [4,2,10].
            - site_saturation (bool, optional): If True, uses site saturation parameters for minimap2. Defaults to False.
            - alignment_name (str, optional): Name of the alignment file. Defaults to "alignment_minimap".

        Returns:
            - None
        """

        fastq_files = output_dir.glob(f"{fastq_prefix}*.fastq")

        if not fastq_files:
            raise FileNotFoundError("No FASTQ files found in the specified output directory.")

        fastq_files_str = " ".join(str(file) for file in fastq_files)

        if site_saturation:
            alignment_name = "alignment_minimap_site_saturation"

            match_score = 4
            mismatch_score = 2
            gap_opening_penalty = 10

            minimap_cmd = f"minimap2 -ax map-ont -A {match_score} -B {mismatch_score} -O {gap_opening_penalty},24 {self.reference_path} {fastq_files_str} > {output_dir}/{alignment_name}.sam"
            subprocess.run(minimap_cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        else:
            minimap_cmd = f"minimap2 -ax map-ont -A {scores[0]} -B {scores[1]} -O {scores[2]},24 {self.reference_path} {fastq_files_str} > {output_dir}/{alignment_name}.sam"
            subprocess.run(minimap_cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        view_cmd = f"samtools view -bS {output_dir}/{alignment_name}.sam > {output_dir}/{alignment_name}.bam"
        subprocess.run(view_cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        sort_cmd = f"samtools sort {output_dir}/{alignment_name}.bam -o {output_dir}/{alignment_name}.bam"
        subprocess.run(sort_cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        index_cmd = f"samtools index {output_dir}/{alignment_name}.bam"
        subprocess.run(index_cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        # Remove SAM file
        os.remove(f"{output_dir}/{alignment_name}.sam")

    def get_variant_df(self, qualities=True, threshold: float = 0.2, min_depth: int = 5, output_dir=''):
        """
        Get Variant Data Frame for all samples in the experiment

        Args:
            - alignment_file (Path): Path to the alignment file (.bam).
            - qualities (bool, optional): If True, include base qualities in the analysis. Defaults to True.
            - threshold (float, optional): Threshold for calling a variant. Defaults to 0.2.
        """
        self.variant_df['P value'] = 1.0
        for i, row in tqdm(self.variant_df.iterrows()):
            if isinstance(row["Path"], os.PathLike):
                bam_file = os.path.join(row["Path"], self.alignment_name)

                # Check if the alignment file exists
                if not os.path.exists(bam_file):
                    # Try aligning the sequences
                    print(f"Aligning sequences for {row['Path']}")
                    self._align_sequences(row["Path"])

                self._apply_alignment_count()

                # Check alignment count
                if self.variant_df["Alignment_count"][i] < min_depth or isinstance(bam_file, float):
                    self.variant_df.at[i, "Variant"] = float("nan")
                    self.variant_df.at[i, "Probability"] = float("nan")
                    continue
                fname = '_'.join(bam_file.split("/")[1:3])
                seq_df = self._get_seq_df([self.ref_name], bam_file, str(self.reference_path),
                                          msa_path=f'{output_dir}msa_{fname}.fa')
                if seq_df is not None:
                    seq_df.to_csv(f'{output_dir}seq_{fname}.csv')
                    # Now use the filter to assign the probabilty that we have larger than the threshold a variant
                    non_refs = seq_df[seq_df['percent_nonRef'] > threshold].sort_values(by='position')
                    if len(non_refs) > 0:
                        positions = non_refs['position'].values
                        refs = non_refs['ref'].values
                        label = [f'{refs[i]}{positions[i] + 1}{actual}' for i, actual in enumerate(non_refs['most_frequent'].values)]
                        label = '_'.join(label)
                        probability = np.mean([x for x in non_refs['percent_nonRef'].values])
                        # Combine the values
                        chi2_statistic, combined_p_value = combine_pvalues([x for x in non_refs['p_value'].values],
                                                                           method='fisher')

                    else:
                        label = '#PARENT#'
                        probability = np.mean([1 - x for x in non_refs['percent_nonRef'].values])
                        combined_p_value = float("nan")
                    self.variant_df.at[i, "Variant"] = label
                    self.variant_df.at[i, "Probability"] = probability
                    self.variant_df.at[i, "P value"] = combined_p_value

                else:
                    self.variant_df.at[i, "Variant"] = float("nan")
                    self.variant_df.at[i, "Probability"] = float("nan")

        # Adjust p-values using bonferroni make it simple
        self.variant_df['P adj. value'] = len(self.variant_df) * self.variant_df["P value"].values
        self.variant_df['P adj. value'] = [1 if x > 1 else x for x in self.variant_df["P adj. value"].values]

        return self.variant_df

    @staticmethod
    def _alignment_from_cigar(cigar: str, alignment: str, ref: str, query_qualities: list) -> tuple[
        str, str, list, list]:
        """
        Generate the alignment from the cigar string.
        Operation	Description	Consumes query	Consumes reference
        0 M	alignment match (can be a sequence match or mismatch)	yes	yes
        1 I	insertion to the reference	yes	no
        2 D	deletion from the reference	no	yes
        3 N	skipped region from the reference	no	yes
        4 S	soft clipping (clipped sequences present in SEQ)	yes	no
        5 H	hard clipping (clipped sequences NOT present in SEQ)	no	no
        6 P	padding (silent deletion from padded reference)	no	no
        7 =	sequence match	yes	yes
        8 X	sequence mismatch	yes	yes

        Parameters
        ----------
        cigar: 49S9M1I24M2D9M2I23M1I3M1D13M1D10M1D13M3D12M1D23M1
        alignment: GCTGATCACAACGAGAGCTCTCGTTGCTCATTACCCCTAAGGAACTCAAATGACGGTTAAAAACTTGTTTTGCT
        ref: reference string (as above but from reference)

        Returns
        -------

        """
        new_seq = ''
        ref_seq = ''
        qual = []
        inserts = []
        pos = 0
        ref_pos = 0
        for op, op_len in cigar:
            if op == 0:  # alignment match (can be a sequence match or mismatch)
                new_seq += alignment[pos:pos + op_len]
                qual += query_qualities[pos:pos + op_len]

                ref_seq += ref[ref_pos:ref_pos + op_len]
                pos += op_len
                ref_pos += op_len
            elif op == 1:  # insertion to the reference
                inserts.append(alignment[pos - 1:pos + op_len])
                pos += op_len
            elif op == 2:  # deletion from the reference
                new_seq += '-' * op_len
                qual += [-1] * op_len
                ref_seq += ref[ref_pos:ref_pos + op_len]
                ref_pos += op_len
            elif op == 3:  # skipped region from the reference
                new_seq += '*' * op_len
                qual += [-2] * op_len
                ref_pos += op_len
            elif op == 4:  # soft clipping (clipped sequences present in SEQ)
                inserts.append(alignment[pos:pos + op_len])
                pos += op_len
            elif op == 5:  # hard clipping (clipped sequences NOT present in SEQ)
                continue
            elif op == 6:  # padding (silent deletion from padded reference)
                continue
            elif op == 7:  # sequence mismatch
                new_seq += alignment[pos:pos + op_len]
                ref_seq += ref[ref_pos:ref_pos + op_len]
                qual += query_qualities[pos:pos + op_len]
                pos += op_len
                ref_pos += op_len
        return new_seq, ref_seq, qual, inserts

    def _get_seq_df(self, positions: dict, bam: str, ref: str, min_coverage=20, k=8, msa_path=None):
        """
        Makes a pileup over a gene.

        Rows are the reads, columns are the columns in the reference. Insertions are ignored.
        Parameters
        ----------
        positions: positions
        bam: bam file read in by pysam, pysam.AlignmentFile(f'data/SRR13212638.sorted.bam', "rb")
        ref: fasta file read in by pysam, pysam.FastaFile(sam/bam file)

        Returns
        -------

        """
        bam = pysam.AlignmentFile(bam, "rb")
        fasta = pysam.FastaFile(ref)
        rows_all = []
        for pos in tqdm(positions):
            reads = []
            try:
                for read in bam.fetch(pos):
                    # Check if we want this read
                    reads.append(read)
            except:
                x = 1

            if len(reads) > min_coverage:
                ref_str = fasta[pos]
                seqs = []
                read_ids = []
                read_quals = []
                for read in reads:
                    if read.query_sequence is not None:
                        seq, ref, qual, ins = self._alignment_from_cigar(read.cigartuples, read.query_sequence, ref_str,
                                                                         read.query_qualities)
                        # Make it totally align
                        seq = "-" * read.reference_start + seq + "-" * (
                                len(ref_str) - (read.reference_start + len(seq)))
                        seqs.append(list(seq))
                        read_ids.append(f'{read.query_name}')
                        read_quals.append(read.qual)

                # Again check that we actually had enough!
                if len(seqs) > min_coverage:
                    seq_df = pd.DataFrame(seqs)
                    # Also add in the read_ids and sort by the quality to only take the highest quality one
                    seq_df['read_id'] = read_ids
                    seq_df['read_qual'] = read_quals
                    seq_df['seqs'] = seqs

                    seq_df = seq_df.sort_values(by='read_qual', ascending=False)
                    # Should now be sorted by the highest quality
                    seq_df = seq_df.drop_duplicates(subset=['read_id'], keep='first')
                    # Reset these guys
                    read_ids = seq_df['read_id'].values
                    seqs = seq_df['seqs'].values

                    seq_df = seq_df.drop(columns=['read_qual', 'read_id', 'seqs'])
                    for col in seq_df:
                        if col - k / 2 > 0:
                            vc = seq_df[col].values
                            ref_seq = ref_str[col]  # Keep track of the reference
                            if ref_seq != '-':
                                # Check if there are at least 25% with a different value compared to the reference.
                                values = len(vc)
                                other = len(vc[vc != ref_seq])
                                a = len(vc[vc == 'A'])
                                t = len(vc[vc == 'T'])
                                g = len(vc[vc == 'G'])
                                c = len(vc[vc == 'C'])
                                nn = len(vc[vc == '-'])
                                km = int(k / 2)
                                kmer = ref_str[col - km:col + km]
                                val = 0.0
                                actual_seq = ref_seq
                                if other == 0:
                                    val = 0.0  # i.e. they were 100% the reference
                                else:
                                    p_b = other/values
                                    if a > 0 and 'A' != ref_seq and a/values > val:
                                        val = a/values
                                        actual_seq = 'A'
                                    if t > 0 and 'T' != ref_seq and t/values > val:
                                        val = t/values
                                        actual_seq = 'T'
                                    if g > 0 and 'G' != ref_seq and g/values > val:
                                        val = g/values
                                        actual_seq = 'G'
                                    if c > 0 and 'C' != ref_seq and c/values > val:
                                        val = c/values
                                        actual_seq = 'C'
                                    if nn > 0 and '-' != ref_seq and nn/values > val:
                                        val = nn/values
                                        actual_seq = 'DEL'
                                # Calculate significance
                                p_a = val
                                # Example values
                                number_of_successes = int(val * values)  # The observed number of changes
                                total_trials = values  # The total number of sequences observed
                                background_error_rate = 0.1  # Background error rate

                                # Perform the binomial test and only check for higher than expected chance
                                p_value = binomtest(number_of_successes, total_trials, background_error_rate, 'greater')
                                rows_all.append([pos, col, ref_seq, actual_seq, p_value.pvalue, val, a, t, g, c, nn, kmer])
                # Check if we want to write a MSA
                if msa_path is not None:
                    with open(msa_path, 'w+') as fout:
                        # Write the reference first
                        fout.write(f'>{self.ref_name}\n{ref_str}\n')

                        for i, seq in enumerate(seqs):
                            fout.write(f'>{read_ids[i]}\n{"".join(seq)}\n')

        bam.close()
        fasta.close()
        if len(rows_all) > 1:  # Check if we have anything to return
            seq_df = pd.DataFrame(rows_all)
            seq_df.columns = ['gene_name', 'position', 'ref', 'most_frequent', 'p_value', 'percent_nonRef', 'A', 'T', 'G', 'C', 'N',
                              'kmer']
            return seq_df

    def _get_ref_name(self):
        with open(self.reference_path, "r") as f:

            # Check if the reference is in fasta format
            ref_name = f.readline().strip()
            if not ref_name.startswith(">"):
                raise ValueError("Reference file is not in fasta format")
            else:
                ref_name = ref_name[1:]
        return ref_name

    def _get_alignment_count(self, sample_folder_path: Path):
        """
        Get the number of alignments in a BAM file.
        
        Args:
            - sample_folder_path (Path): Path to the folder containing the BAM file.
            
        Returns:
            - int: Number of alignments in the BAM file.
        """
        if not isinstance(sample_folder_path, Path):
            return 0

        bam_file = os.path.join(sample_folder_path, self.alignment_name)

        if not os.path.exists(bam_file):
            return 0

        try:
            alignment_count = int(
                subprocess.run(f"samtools view -c {bam_file}", shell=True, capture_output=True).stdout.decode(
                    "utf-8").strip())
        except:
            # ToDo: Return a meaningful error here
            print(f'Warning! your bamfile: {bam_file} had no counts! Check the header manually.')
            return 0
        return alignment_count

    def _apply_alignment_count(self):
        """
        Get alignment count for each sample
        """

        self.variant_df["Path"] = self.variant_df["Path"].apply(lambda x: Path(x) if isinstance(x, str) else x)

        self.variant_df["Alignment_count"] = self.variant_df["Path"].apply(self._get_alignment_count)

        return self.variant_df

    def _get_postion_range(self, padding_start: int = 0, padding_end: int = 0):
        """
        Get the positions of the non-reference bases in the reference sequence.

        Args:
            - padding_start (int, optional): Number of bases to pad at the start of the reference sequence. Defaults to 0.
            - padding_end (int, optional): Number of bases to pad at the end of the reference sequence. Defaults to 0.
        
        Returns:
            - list: List of positions of the non-reference bases in the reference sequence.
        """

        return range(padding_start + 1, len(self.reference) - padding_end + 1)

    def _call_potential_populations(self, softmax_df, call_threshold: float = 0.1):
        """

        """
        positions = softmax_df.columns
        top_combinations = []

        # Get the top 2 variants for each position
        for position in positions:
            top_variants = softmax_df[position].nlargest(2)

            if top_variants.iloc[1] < call_threshold:
                top_combinations.append([top_variants.index[0]])

            else:
                top_combinations.append(top_variants.index.tolist())

            potential_combinations = list(itertools.product(*top_combinations))

        variants = {"Variant": [], "Probability": []}

        for combination in potential_combinations:
            final_variant = []
            for i, pos in enumerate(positions):

                if combination[i] == self.reference[pos - 1]:
                    continue

                elif combination[i] == "-":
                    var = f"{self.reference[pos - 1]}{pos}DEL"
                    final_variant.append(var)
                else:
                    var = f"{self.reference[pos - 1]}{pos}{combination[i]}"
                    final_variant.append(var)

            final_variant = '_'.join(final_variant)
            if final_variant == "":
                final_variant = "#PARENT#"

            joint_prob = VariantCaller.joint_probability_score(softmax_df, combination, positions)
            # TODO: Add calculate score function, so different type of scores can be used:
            # Input: Softmax_df
            # Output: Variant name with Score

            variants["Variant"].append(final_variant)
            variants["Probability"].append(joint_prob)

        return variants

    def _get_neighbouring_position(self, position: int, neighbour_range: int = 2):
        """
        Get the neighbouring positions of the non-reference bases in the reference sequence.

        Args:
            - positions (list): List of positions of the non-reference bases in the reference sequence.
            - neighbour_range (int, optional): Range of neighbouring positions to consider. Defaults to 2.
        
        Returns:
            - list: List of neighbouring positions of the non-reference bases in the reference sequence.
        """

        # Get min range and max range

        pos_range = self._get_postion_range(padding_start=self.padding_start, padding_end=self.padding_end)

        min_range = min(pos_range)
        max_range = max(pos_range)

        if position < min_range or position > max_range:
            raise ValueError(
                f"Position {position} is out of range. The position should be between {min_range} and {max_range}.")

        neighbouring_positions = list(range(position - neighbour_range, position + neighbour_range + 1))

        neighbouring_positions = [pos for pos in neighbouring_positions if pos >= min_range and pos <= max_range]

        return neighbouring_positions

    @staticmethod
    def _get_non_error_prop(quality_score):
        """
        Convert quality score to non-error probability.
        
        Args:
            - Phred quality_score (int): Quality score.
        
        Returns:
            - float: Non-error probability.
        """
        return 1 - 10 ** (-quality_score / 10)

    @staticmethod
    def joint_probability_score(softmax_df, combination, positions):
        """
        Calculate the joint probability score for a given combination of variants.

        Args:
            - softmax_df (pd.DataFrame): Softmax count dataframe.
        
        Returns:
            - float: Joint probability score.
        """
        return np.prod([softmax_df.at[combination[i], positions[i]] for i in range(len(positions))])

    @staticmethod
    def joint_log_probability_score(softmax_df, combination, positions):
        """
        Calculate the joint probability score for a given combination of variants.

        Args:
            - softmax_df (pd.DataFrame): Softmax count dataframe.
        
        Returns:
            - float: Joint probability score.
        """
        return np.sum([np.log(softmax_df.at[combination[i], positions[i]]) for i in range(len(positions))])


def get_template_df(plate_numbers: list, barcode_dicts: dict = None, rowwise=True):
    """
    To have coherent df for each experiment, a template df is created. The template also have the desired plates and columns in the desired order
    Input:
        - demultiplex_folder, folder where the demultiplexed files are located
        - rowwise, if True, the reverse barcodes are rows and not plates
    """

    if barcode_dicts is None:
        raise ValueError("No barcode dictionary provided")

    n_rbc = len(barcode_dicts.items())

    rows = ["A", "B", "C", "D", "E", "F", "G", "H"]
    columns = [i for i in range(1, 13)]

    if rowwise:
        template = {"Plate": [], "Well": []}

        for row in rows:
            for column in columns:
                template["Plate"].append(1)
                template["Well"].append(f"{row}{column}")

    else:

        template = {"Plate": [], "Well": []}

        for i in range(n_rbc):
            for row in rows:
                for column in columns:
                    template["Plate"].append(plate_numbers[i])
                    template["Well"].append(f"{row}{column}")

    return pd.DataFrame(template)
