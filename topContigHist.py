#!/usr/bin/env python

# print size of top10 contigs
# Matthew J. Neave 31.7.17 

from Bio import SeqIO
import sys

contig_file = open(sys.argv[1])

num_to_print = 10
count = 0

for record in SeqIO.parse(contig_file, "fasta"):
    count += 1
    print(len(record.seq))
    if count == 1:
        longest_contig = len(record.seq)
        print("|" * 80)
    else:
        current_len = len(record.seq)
        current_perc = (current_len/longest_contig)*100
        print("|" * int(current_perc * 0.8))
    if count >= num_to_print:
        break
