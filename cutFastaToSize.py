#!/usr/bin/env python
# python 3

# Matthew J. Neave 17.12.15
# script to cut a large fasta file into selected sizes
# can then run several blasts, etc at once

import sys
import argparse
from Bio import SeqIO # requires biopython

# use argparse for command line arguments

parser = argparse.ArgumentParser("cut fasta file into chunks of selected size")

parser.add_argument("input_fasta", type = argparse.FileType("r"), nargs = 1, 
        help = "input fasta file to split")
parser.add_argument("seqs_per_file", type = int, nargs = 1, 
        help = "number of sequences in each split file")

args = parser.parse_args()

# now read through fasta file and create new output every selected size

fasta_seqs = SeqIO.parse(args.input_fasta[0], "fasta")

count = 0
file_num = 1
output_file = open("fasta_chunk_1", "w")

for seq in fasta_seqs:
    if count < args.seqs_per_file[0]:
        SeqIO.write(seq, output_file, "fasta")
        count += 1
    else:
        count = 1
        file_num += 1
        output_file = open("fasta_chunk_" + str(file_num), "w")
        SeqIO.write(seq, output_file, "fasta")

print("Created %s files each containing %s sequences, except the last which contains the remaining %s sequences" % (file_num, args.seqs_per_file[0], count))
