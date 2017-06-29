#!/usr/bin/env python
# python 3
# script to sort mixed file  after trimming
# Matthew J. Neave 5.5.2015 <matthewjneave1@gmail.com>

# library imports

import sys
import argparse
from Bio.SeqIO.QualityIO import FastqGeneralIterator # requires Biopython

# use argparse to grab command line arguments

parser = argparse.ArgumentParser("sort mixed fastq file into paired and unpaired sequences")

parser.add_argument('mixed_reads', type = argparse.FileType("r"),
        nargs = "?", help = "fastq file containing mix of forward, reverse and unpaired reads")
parser.add_argument('output_prefix', type = str,
        nargs = "?", help = "a name to prefix the output files")

args = parser.parse_args()
forward_handle = open(args.output_prefix + ".R1.fastq", "w")
reverse_handle = open(args.output_prefix + ".R2.fastq", "w")
orphan_handle = open(args.output_prefix + ".orphan.fastq", "w")

print("Scanning mixed file and building list of names...")
forward_ids = set()
reverse_ids = set()

for title, seq, qual in FastqGeneralIterator(args.mixed_reads):
    name = title.split()[0]
    pair = title.split()[1]
    if pair.startswith("1"):
        forward_ids.add(name)
    if pair.startswith("2"):
        reverse_ids.add(name)

args.mixed_reads.seek(0)    # moves back to start of file
print("writing files")

for title, seq, qual in FastqGeneralIterator(args.mixed_reads):
    name = title.split()[0]
    pair = title.split()[1]
    if name in reverse_ids and name in forward_ids:
        # paired reads
        if pair.startswith("1"): 
            forward_handle.write("@%s\n%s\n+\n%s\n" % (title, seq, qual))
        if pair.startswith("2"):
            reverse_handle.write("@%s\n%s\n+\n%s\n" % (title, seq, qual))
    else:
        # orphan reads
        orphan_handle.write("@%s\n%s\n+\n%s\n" % (title, seq, qual))

print("done")
