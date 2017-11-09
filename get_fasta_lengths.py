#!/usr/bin/env python
# python 3

# get lengths of each contig in fasta file
# write lengths out in 2 column text file (name + length)
# Matthew J. Neave

import sys
from Bio import SeqIO

fasta = SeqIO.parse(sys.argv[1], "fasta")
output = open(sys.argv[2], "w")

for seq in fasta:
    output.write(seq.name + "\t" + str(len(seq)) + "\n")
