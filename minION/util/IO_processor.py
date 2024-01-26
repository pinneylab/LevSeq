# This script contains function to check for input data and process it for downstream analysis.

import os
import glob
from minION.util.globals import MINKNOW_PATH
from Bio import SeqIO
from pathlib import Path
import gzip
import subprocess

def check_data_folder(path : Path) -> None:
    """
    Check if minknown data folder exists. If not, assert an error.

    Args:
    - path (str): The path to the minknow data folder.

    Returns:
    - FileNotFoundError: If the minknow data folder does not exist.
    """
    if not path.exists():
        raise FileNotFoundError(f"MinKNOW data folder '{path}' does not exist. Please check if you have installed MinKNOW and if the path is correct. If you replaced the default path, please specify in the TOML file.")

def find_experiment_folder(experiment_name : str, minknow_path : Path = MINKNOW_PATH) -> None:
    """Find the experiment folder in the minknow data folder. Access the name from Meta File.
    
    Args:
    - experiment_name (str): The name of the experiment to search for.
    - minknow_path (str): The path to the minknow data folder.

    Returns:
    - str: The full path to the found experiment folder.
    """

    check_data_folder(Path(minknow_path))

    for (path, dirs, files) in os.walk(minknow_path, topdown=True):
        if experiment_name in dirs:
            return os.path.join(path, experiment_name)
        
    
    raise Exception("Experiment folder does not exist. Please check if you have chosen the right experiment name.")


def find_folder(start_path, target_folder_name):
    """
    Find a specific folder within the start_path. Access the name from Meta File.
    
    Args:
    - start_path (str): The path to begin the search from.
    - target_folder_name (str): The name of the folder to search for.

    Returns:
    - str: The full path to the found folder.
    - Exception: If the target folder is not found.
    """
    for (path, dirs, _) in os.walk(start_path, topdown=True):
        if target_folder_name in dirs:
            return os.path.join(path, target_folder_name)
    raise Exception(f"{target_folder_name} folder does not exist. Please check if you have chosen the right name.")


def find_experiment_files(start_path : Path, target_folder_name : list) -> Path or None:
    """
    Check if the experimenter has already basecalled before. If pod5_pass or fastq_pass folder exists, the function returns True.

    Args:
        - start_path (Path): The path to begin the search from.
        - target_folder_name (str): The name of the folder to search for.

    Returns:
        - Target folder (Path): The full path to the found folder.
        - False: If the target folder is not found.

    """

    for value in target_folder_name:
        try:
            return find_folder(start_path, value)
        except:
            continue
      
    return None

def extract_files_from_folder(path : Path) -> list:
    """Extract all files from a folder"""
    return [file for file in path.iterdir() if file.is_file()]


def filter_fastq_by_length(input_fastq : Path, output_fastq : Path, min_length : int , max_length : int):
    """
    Filter a FASTQ file based on read length and write to a new FASTQ file.

    Args:
        - input_fastq: Path to the input FASTQ gzip file.
        - output_fastq: Path to the output FASTQ gzip file.
        - min_length: Minimum length of reads to retain.
        - max_length: Maximum length of reads to retain.
    Returns:
        - Fastq file with reads between min_length and max_length.
        - N_reads
    """
    with gzip.open(input_fastq, 'r') as infile, open(output_fastq, 'w') as outfile:

        while True:
            
            header = infile.readline().strip()
            sequence = infile.readline().strip()
            plus_sign = infile.readline().strip()
            quality_scores = infile.readline().strip()

            if not header:
                break
            N_reads = 0
            if min_length <= len(sequence) <= max_length:
                outfile.write(f"{header}\n")
                outfile.write(f"{sequence}\n")
                outfile.write(f"{plus_sign}\n")
                outfile.write(f"{quality_scores}\n")
                N_reads += 1
    
    return N_reads

def find_file(start_path : Path, prefix : str, extension : str) -> Path:
    """
    Find a file in the given start_path that matches the specified prefix and extension.
    
    Args:
    - start_path (str): The directory to begin the search from.
    - prefix (str): The prefix of the filename to search for.
    - extension (str): The extension of the file to search for (e.g., '.txt').

    Returns:
    - str: The full path to the found file.
    
    Raises:
    - Exception: If no matching file is found.
    """
    
    for dirpath, _, filenames in os.walk(start_path):
        for filename in filenames:
            if filename.startswith(prefix) and filename.endswith(extension):
                return os.path.join(dirpath, filename)
    
    raise Exception(f"No file with prefix '{prefix}' and extension '{extension}' was not found in {start_path}.")



def concatenate_fastq_files(path: Path, filename: str = "concatenated", prefix: str = "*", delete: bool = True) -> str:
    """
    Concatenate all fastq files in a directory.
    
    Args:
        - path (Path): Directory where fastq files are located.
        - filename (str): Name of the concatenated file. Default is 'concatenated'.
        - prefix (str): Prefix of files to be concatenated. Default is '*' (all files).
        - delete (bool): Whether to delete the original files after concatenation.
    
    Returns:
        - str: Message indicating the result of the operation.
    """
    search_pattern = path / f"{prefix}.fastq"
    fastq_files = [Path(p) for p in glob.glob(str(search_pattern))]

    if not fastq_files:
        return "No fastq files found."

    if len(fastq_files) == 1:
        single_file = fastq_files[0]

        if single_file.name != f"{filename}.fastq":
            target_path = path / f"{filename}.fastq"
            
            if target_path.exists():
                return f"Target file {target_path} already exists. Rename operation aborted."

            single_file.rename(target_path)
            return f"Single fastq file in {path} found and renamed."

    else:
        # Concatenate multiple files
        target_path = path / f"{filename}.fastq"

        if target_path.exists():
            return f"Target file {target_path} already exists. Concatenation aborted."

        with target_path.open("w") as outfile:
            for fastq_file in fastq_files:
                with fastq_file.open() as infile:
                    outfile.write(infile.read())

        if delete:
            for fastq_file in fastq_files:
                fastq_file.unlink()

        return "Concatenation successful."


def read_fasta_file(path : Path, score = False) -> dict:
    """
    Read fasta file from an input path

    Args:  
        - path, where the fasta file is located
        - score, if True, return sequence and quality scores

    Returns: 
        - Dictionary with sequence only or sequence and quality scores
    """

    if score:
        sequences_and_scores = {"Sequence" : [], "Quality-Score" : []}

        for record in SeqIO.parse(path, "fastq"):
            sequences_and_scores["Sequence"].append(str(record.seq))
            sequences_and_scores["Quality-Score"].append(record.letter_annotations["phred_quality"])

        return sequences_and_scores

    else:
        sequences = {"Sequence" : []}

        file_extension = os.path.splitext(path)[1][1:] # Get file extension
        
        for record in SeqIO.parse(path, "fasta"):
            sequences["Sequence"].append(str(record.seq))

        return sequences



def create_folder(experiment_name: str, dorado_model, target_path: Path = None, output_name: str = None) -> Path:
    """
    When Starting minION, the function checks if a minION result folder exists. If not, it creates one. 
    It also checks for the subfolder of the experiment.
    If no information is given about the folder, it creates a default folder in the current directory.
    
    Args:

    - target_path, path of the folder to be created

    Returns: 

    - Path object representing the experiment folder
    - Raises Exception if the folder could not be created or path is invalid
    """
    
    if target_path is None:
        # Get current working directory
        curr_dir = Path.cwd()
    else:
        if not target_path.exists():
            raise Exception("Target path does not exist. Please check if you have chosen the right path.")
        curr_dir = target_path
    
    # Create minION_results folder if it doesn't exist
    minION_results_dir = curr_dir / "minION_results"
    minION_results_dir.mkdir(exist_ok=True)
    
    # Create experiment folder

    experiment_name = f"{experiment_name}_{dorado_model}"

    if output_name is None:
        result_folder = minION_results_dir / experiment_name
    else:
        output_name = f"{output_name}_{dorado_model}"
        result_folder = minION_results_dir / output_name

    result_folder.mkdir(exist_ok=True)

    return result_folder

    
def get_rbc_barcode_folders(demultiplex_folder: Path, prefix = "barcode") -> list:
    """Extract the reverse barcode folders (rbc) from the demultiplex folder
    Args:
    - demultiplex_folder (Path): Where the demultiplex folder is located.
    Returns:
    - reverse_barcodes (list): Where the barcode folders are located. 
    """

    if not demultiplex_folder.exists():
        raise FileNotFoundError(f"Demultiplex folder '{demultiplex_folder}' does not exist. Run minION to get the demultiplex folder.")
    
    reverse_barcodes = list(demultiplex_folder.glob(f"{prefix}*"))

    if not reverse_barcodes:
        # Optionally, use logging here instead of raising an exception
        raise FileNotFoundError(f"No reverse barcodes found in {demultiplex_folder}. Either no barcodes were found or the barcode score is too high. Rerun the experiment or adapt the barcode score in the TOML file.")
    
    return reverse_barcodes

def get_fbc_barcode_folders(rbc_barcode_folders : list, prefix = "barcode") -> dict:
    """Extract the forward barcode folders (fbc) within the reverse barcode folders

    Args:  
    - result_folder, where the demultiplex folder is located
    - rbc_barcode_folders, name of reverse barcode folders

    Returns: 
    - Barcode folders (dict), where the forward barcode folders are located    
    """

    fbc_folders = {}

    if rbc_barcode_folders is None:
        raise Exception("Reverse barcode folders are not given. Please check if you have chosen the right path.")
    
    for folder in rbc_barcode_folders:
        
        fbc_folders[folder] = list(folder.glob(f"{prefix}*"))

    if not fbc_folders:
        raise Exception(f"Forward barcodes in {rbc_barcode_folders} do not exist. Either no barcodes were found or the barcode score is too high. Rerun the experiment or adapt the barcode score in the TOML file. ")
    
    if not any(fbc_folders.values()):
        raise Exception(f"Forward barcodes in {rbc_barcode_folders} do not exist. Please check the folders.")
    
    return fbc_folders
    
    return fbc_folders

def get_barcode_dict(demultiplex_folder : Path, front_prefix = "barcode", reverse_prefix = "barcode") -> dict:
    """
    Get a dictionary of folder paths, where reverse is the key and forward is stored in a list
    
    Args:
    - demultiplex_folder, where the demultiplex folder is located
    
    Returns:
    - barcode_dict, dictionary of reverse and front barcode paths
    """

    rbc_folders = get_rbc_barcode_folders(demultiplex_folder, prefix = reverse_prefix)
    fbc_folders = get_fbc_barcode_folders(rbc_folders, prefix = front_prefix)

    return fbc_folders

def trim_fasta(input_file, output_file, trim_length=12):
    with open(input_file, 'r') as in_fasta, open(output_file, 'w') as out_fasta:
        for record in SeqIO.parse(in_fasta, 'fasta'):
            trimmed_seq = record.seq[trim_length:]
            record.seq = trimmed_seq
            SeqIO.write(record, out_fasta, 'fasta')



def filter_fastq_by_length(result_folder, input_fastq : Path, min_length : int , max_length : int, ind : int):
    """
    Filter a FASTQ file based on read length and write to a new FASTQ file. Currently we use fastq-filter.

    Args:
        - input_fastq: Path to the input FASTQ file or folder.
        - output_fastq: Path to the output FASTQ file.
        - min_length: Minimum length of reads to retain.
        - max_length: Maximum length of reads to retain.
    Returns:
        - Fastq file with reads between min_length and max_length.
        - N_reads
    """
    
    if input_fastq.is_dir():
        input_files = f'{input_fastq}/*.fastq'

    elif input_fastq.is_file():
        input_files = input_fastq
    
    else:
        raise Exception("Input file is not a file or a folder. Please check if you have chosen the right path.")
    

    basecall_folder = os.path.join(result_folder, "basecalled_filtered")
    Path(basecall_folder).mkdir(parents=True, exist_ok=True)

    prompt = f'fastq-filter -o {basecall_folder}/basecalled_filtered{ind}.fastq.gz -l {min_length} -L {max_length} {input_files} --quiet'

    subprocess.run(prompt, shell=True)
    


