#!/usr/bin/env python

# take raw NGS reads, trim, calc kmer peak, and draw graph
# Matthew J. Neave 21.06.2018

import argparse
import subprocess # use to pass command line calls

# argparse to collect command line arguments

parser = argparse.ArgumentParser("take raw NGS reads, trim, calculate 31-mer peaks, and produce a graph\nnote: requires cutadapt, trimgalore and bbmap to be present on the path\n")

parser.add_argument('-1', '--forward_reads', type = str,
        nargs=1, help = "raw fastq forward reads")
parser.add_argument('-2', '--reverse_reads', type = str,
        nargs=1, help = "raw fastq reverse reads")

args = parser.parse_args()

# grab stem name of files for later

stem = args.forward_reads[0].split("_")[0]

# the reads first need to be trimmed
# will use cutadapt / trimgalore because adapters will be
# automatically detected 

subprocess.call(["trim_galore", "--fastqc", "--length", "50", "--trim-n", "--paired", args.forward_reads[0], args.reverse_reads[0]], shell=False)

forward_trimmed = args.forward_reads[0].rstrip(".fastq.gz") + "_trimmed.fq.gz"
reverse_trimmed = args.reverse_reads[0].rstrip(".fastq.gz") + "_trimmed.fq.gz"

# now use bbmap's khist to draw kmer profile

subprocess.call(["khist.sh", "in=" + forward_trimmed, "in2=" + reverse_trimmed, "khist=" + stem + "khist.txt", "threads=16", "k=31"])


