# Variant Sequencing with Nanopore

In directed evolution, sequencing every variant enhances data insight and creates datasets suitable for AI/ML methods. This method is presented as an extension of the original Every Variant Sequencer using Illumina technology. With this approach, sequence variants can be generated within a day at an extremely low cost.

![Figure 1: LevSeq Workflow](manuscript/figures/LevSeq_Figure-1.png)
Figure 1: Overview of the LevSeq variant sequencing workflow using Nanopore technology. This diagram illustrates the key steps in the process, from sample preparation to data analysis and visualization.


- Data to reproduce the results and to test are available on zenodo [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.13694463.svg)](https://doi.org/10.5281/zenodo.13694463)
- A dockerized website and database for labs to locally host and visualize their data: website is available [here](https://github.com/ArianeMora/LevSeq_vis/) and code to host locally at: https://github.com/fhalab/LevSeq_VDB/

## Setup

For setting up the experimental side of LevSeq we suggest the following preparations:

- Order forward and reverse primers compatible with the desired plasmid, see methods section of [our paper](http://biorxiv.org/cgi/content/short/2024.09.04.611255v1?rss=1).
- Successfully install Oxford Nanopore's software (this is only for if you are doing basecalling/minION processing). [Link to installation guide](https://nanoporetech.com/).

## How to Use LevSeq

The wet lab part is detailed in the method section of the paper or via the [wiki](https://github.com/fhalab/LevSeq/wiki/Experimental-protocols).

Once samples are prepared, the multiplexed sample is used for sequencing, and the sequencing data is stored in the `../data` folder as per the typical Nanopore flow (refer to Nanopore documentation for this).

After sequencing, you can identify variants, demultiplex, and combine with your variant function here! For simple applications, we recommend using the notebook `example/Example.ipynb`.

### Installation on Wynton
These steps need to be run on a Wynton dev node! The login nodes have the correct versions of `make` or `cmake` installed. 

1. Create and activate a `levseq` conda environment with `conda create --name levseq python=3.12 -y` and `conda activate levseq`.
2. Install Samtools and Minimap2 with `conda install -c bioconda -c conda-forge samtools` and `conda install -c bioconda -c conda-forge minimap2`.
3. Install `g++` and `gcc` compilers as well as `zlib` with `conda install -c conda-forge gcc=13 gxx=13 zlib`.
4. Within the `executable` directory, create a `build` directory. Enter this directory and build the project using `cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_C_COMPILER=gcc -DCMAKE_CXX_COMPILER=g++ ../source/`.
5. Run `make -j` within the `build` directory. This should create a new subdirectory, `bin`, where you will find the compiled binaries for the demultiplexing code!

Now you should be able to run the entire pipeline on Wynton.


### Docker Installation (Recommended for full pipeline)  
Coming soon!


### Usage
`levseq` arguments are passed using a configuration file. A template is provided in `config.yml`. 

Required arguments:
- `name`: a descriptive name for the run
- `fasta_dir`: path to directory containing nanoPore reads in fastq format
- `summary_csv`: path to csv file containing plate information
- `working_dir`: path to directory where output files should be dumped
- `barcode_path`: path to fasta file containing barcode sequences

Demultiplexing arguments:
- `front_window_size`: specifies the length of the 5` window on reads to which the forward barcode is aligned to.
- `rear_window_size`: same as above, but for the 3` window and reverse barcode.
- `min_read_length`: toss out reads under this threshold
- `max_read_length`: toss out reads above this threshold
- `alignment_score_threshold`: ignore alignments between barcode and reads with a score below this threshold
- `edit_distance_threshold`: ignore alignments between barcode and reads that are greater than this threshold

Variant calling arguments:
- `position_offset`: useful if you want to update the indexing of your amino acid sequence
- `calling_threshold`: treat reads containing the same barcodes as WT if the percentage of reads containing a specific mutation is less than this threshold
- `n_threads`: number of threads to use during variant calling

Miscelanious agruments:
- `skip_demultiplexing`
- `skip_variantcalling`
- `show_msa`: specifies whether or not to include sequence alignments of reads for each well in final output figure (may take a long time to generate this figure if you have multiple plates)

#### Run locally
```
levseq /path/to/config.yml
```

#### Run with docker
Coming soon!

#### Citing

If you have found LevSeq useful, please cite out [paper](https://doi.org/10.1101/2024.09.04.611255).
