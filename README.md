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

### Installation

We aimed to make LevSeq as simple to use as possible, this means you should be able to run it all using pip (note you need `samtools` 
and `minimap2` installed on your path. However, if you have issues we recommend using the Docker instance! 
(the pip version doesn't work well with mac M3 but docker does.)

We recommend using terminal and a conda environment for installation:

```
conda create --name levseq python=3.12 -y
```

```
conda activate levseq
```

#### Dependencies 

1. Samtools: https://www.htslib.org/download/ 
```
conda install -c bioconda -c conda-forge samtools
```
or for mac users you can use: `brew install samtools`

2. Minimap2: https://github.com/lh3/minimap2

```
conda install -c bioconda -c conda-forge minimap2
```

### Docker Installation (Recommended for full pipeline)  
For installing the whole pipeline, you'll need to use the docker image. For this, install docker as required for your 
operating system (https://docs.docker.com/engine/install/).

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

#### Run locally
```
levseq /path/to/config.yml
```

#### Run with docker
If using linux system
```
docker pull yueminglong/levseq:levseq-1.2.5-x86
```
If using Mac M chips (image tested on M1, M3, and M4)
```
docker pull yueminglong/levseq:levseq-1.2.5-arm64
```

```
docker run --rm -v "$(pwd):/levseq_results" yueminglong/levseq:levseq-1.2.5-<architecture> <name> <location to data folder> <location of reference csv file>
```
Explanation:

--rm: Automatically removes the container after the command finishes.

-v "$(pwd):/levseq\_results": Mounts the current directory ($(pwd)) to /levseq\_results inside the container, ensuring the results are saved to your current directory.

yueminglong/levseq:levseq-1.2.5-\<architecture\>: Specifies the Docker image to run. Replace \<architecture\> with the appropriate platform (e.g., x86).

\<name\>: The name or identifier for the analysis.

\<location to data folder\>: Path to the folder containing input data.

\<location of reference csv file\>: Path to the reference .csv file.

Important Notes:

If the current directory is mounted to the container (via -v "$(pwd):/levseq\_results"), the basecalled result in FASTQ format and the ref.csv file must be located in the current directory.

If these files are not present in the current directory, they will not be processed by the tool.

#### Citing

If you have found LevSeq useful, please cite out [paper](https://doi.org/10.1101/2024.09.04.611255).
