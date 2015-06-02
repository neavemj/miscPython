#!/usr/bin/env python

# extracts a subset of sequences from a sam file using a list of target contigs
# Matthew J. Neave 2.6.15

import argparse

# get command line arguments with argparse

parser = argparse.ArgumentParser("gets reads from sam file that map to particular contigs")

parser.add_argument("sam_file", type = argparse.FileType("r"), nargs = 1,
        help = "sam file to extract reads from")
parser.add_argument("contig_list", type = argparse.FileType("r"), nargs = 1,
        help = "extract reads that match to these contigs")
parser.add_argument("output_name", type = argparse.FileType("w"), nargs = 1,
        help = "fasta file output name")

args = parser.parse_args()


# create list of target contigs

target_contigs = []

for contig in args.contig_list:
    contig = contig.strip()
    target_contigs.append(contig)

# now extract reads that map to these contigs and write to fasta















