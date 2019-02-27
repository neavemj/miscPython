#!/usr/bin/env python

# script to extract reads in fastq format from list of read headers
# Matthew J. Neave 09.03.2018 <matthewjneave1@gmail.com>
# python 3

# library imports

import sys
import argparse
from Bio.SeqIO.QualityIO import FastqGeneralIterator # requires Biopython

# use argparse to grab command line arguments

parser = argparse.ArgumentParser("extract fastq reads given a list of headers")

parser.add_argument('-l', '--headers', type = argparse.FileType("r"),
        nargs = "?", help = "text file containing wanted headers")
parser.add_argument('-1', '--forward_reads', type = argparse.FileType("r"),
        nargs = "?", help = "fastq file containing forward R1 reads")
parser.add_argument('-2', '--reverse_reads', type = str,
        nargs = "?", help = "fastq file containing reverse R2 reads")
parser.add_argument('-o', '--output_prefix', type = str,
        nargs = "?", help = "a name to prefix the output files")

args = parser.parse_args()
forward_handle = open(args.output_prefix + ".R1.fastq", "w")
reverse_handle = open(args.output_prefix + ".R2.fastq", "w")

print("Building list of wanted headers")
wanted_ids = set([line.strip().lstrip("@") for line in args.headers])

print("Scanning reverse file and building list of names...")
reverse_ids = set()
paired_ids = set()
for title, seq, qual in FastqGeneralIterator(open(args.reverse_reads)):
    reverse_ids.add(title.split()[0])

print("Processing forward file")

for title, seq, qual in FastqGeneralIterator(args.forward_reads):
    name = title.split()[0]
    if name in reverse_ids \
    and name in wanted_ids:
        # paired wanted reads
        paired_ids.add(name)
        reverse_ids.remove(name) # saves a little memory
        forward_handle.write("@%s\n%s\n+\n%s\n" % (title, seq, qual))
forward_handle.close()

print("Processing reverse file")

for title, seq, qual in FastqGeneralIterator(open(args.reverse_reads)):
    name = title.split()[0]
    if name in paired_ids:
        # paired reads
        reverse_handle.write("@%s\n%s\n+\n%s\n" % (title, seq, qual))
reverse_handle.close()

print("done")
