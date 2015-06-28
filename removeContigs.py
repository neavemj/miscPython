#!/usr/bin/env python

# script to remove contigs below a certain threshold length
# Matthew J. Neave 28.6.15

from Bio import SeqIO
import sys


contig_file = open(sys.argv[1])
req_length = int(sys.argv[2])
output = open(sys.argv[3], "w")

wanted = []

for record in SeqIO.parse(contig_file, "fasta"):
    if len(record.seq) > req_length:
        wanted.append(record)

SeqIO.write(wanted, output, "fasta")
output.close()
