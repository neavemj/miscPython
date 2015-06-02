#!/usr/bin/env python

# extracts a subset of sequences from a sam file using a list of target contigs
# Matthew J. Neave 2.6.15

import argparse
import re 

"""
uses regex to match header names so need to be careful with contig list
eg. NODE_1 also matches NODE_100, put following character to avoid
NODE_1_ no longer matches higher up numbers
"""

# get command line arguments with argparse

parser = argparse.ArgumentParser("gets reads from sam file that map to particular contigs")

parser.add_argument("sam_file", type = argparse.FileType("r"), nargs = 1,
        help = "sam file to extract reads from")
parser.add_argument("contig_list", type = argparse.FileType("r"), nargs = 1,
        help = "extract reads that match to these contigs")
parser.add_argument("output", type = argparse.FileType("w"), nargs = 1,
        help = "fasta file output name")

args = parser.parse_args()


# create list of target contigs

target_contigs = []

for contig in args.contig_list[0]:
    contig = contig.strip()
    target_contigs.append(contig)

# now extract reads that map to these contigs and write to fasta

for record in args.sam_file[0]:
    record = record.strip()
    cols = record.split("\t")
    if not record.startswith("@"):
        for contig in target_contigs:
            if re.search(contig, cols[2]): # see note about regex
                args.output[0].write(">%s\n%s\n" % (cols[0], cols[9]))
