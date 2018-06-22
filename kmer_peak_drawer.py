#!/usr/bin/env python

# take raw NGS reads, trim, calc kmer peak, and draw graph
# Matthew J. Neave 21.06.2018

import argparse
import subprocess # use to pass command line calls
import os

# argparse to collect command line arguments

parser = argparse.ArgumentParser("take raw NGS reads, trim, calculate 31-mer peaks, and produce a graph\nnote: requires trimmomatic and bbmap to be present on the path\n")

parser.add_argument('-1', '--forward_reads', type = str,
        nargs=1, help = "raw fastq forward reads")
parser.add_argument('-2', '--reverse_reads', type = str,
        nargs=1, help = "raw fastq reverse reads")
parser.add_argument('-t', '--threads', type = str,
        nargs="?", default="16", help = "threads for trimming and khist [default 16]")

args = parser.parse_args()

# check that trimmomatic adapters are present (CSIRO modules location)

try:
    adapter_fl = open("/apps/trimmomatic/0.36/adapters/TruSeq3-PE-2.fa")
    adapter_path = "/apps/trimmomatic/0.36/adapters/TruSeq3-PE-2.fa"
    print("~ found adapter files ~")
except:
    print("\n~ could not find adapter file for trimmomatic! ~\n")
    raise

# grab stem name of files for later

stem = args.forward_reads[0].split("_")[0]

# the reads first need to be trimmed
print("~~~ beginning trimming with trimmomatic ~~~")

subprocess.call(["trimmomatic", "PE", "-threads", args.threads, args.forward_reads[0], args.reverse_reads[0], "-baseout", stem+".fastq.gz", "ILLUMINACLIP:" + adapter_path + ":2:30:10", "LEADING:3", "TRAILING:3", "SLIDINGWINDOW:4:20", "MINLEN:50"])

forward_trimmed = args.forward_reads[0].rstrip("R1.fastq.gz") + "1P.fastq.gz"
reverse_trimmed = args.reverse_reads[0].rstrip("R2.fastq.gz") + "2P.fastq.gz"

# now use bbmap's khist to draw kmer profile

print("~~~ beginning kmer profile with bbmap ~~~")

subprocess.call(["khist.sh", "in=" + forward_trimmed, "in2=" + reverse_trimmed, "khist=" + stem + ".khist.txt", "threads=16", "k=31"])


