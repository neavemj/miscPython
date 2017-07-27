#!/usr/bin/env python
# python 3

# Matthew J Neave 30.06.2017
# extract sequences using a list of IDs
# input fasta first, then seq IDs, then a name for the output
# keep the list order in this case (handy for mauve re-ordering)

import sys
from Bio import SeqIO

fasta_file = sys.argv[1]  # input fasta file
number_file = sys.argv[2] # list of sequence IDs of interest
result_file = open(sys.argv[3], "w") # output name

records = SeqIO.to_dict(SeqIO.parse(fasta_file, "fasta"))
new_records = []

with open(number_file) as wanted:
    for line in wanted:
        line = line.strip()
        if line in records:
           result_file.write(">" + records[line].id + "\n" + str(records[line].seq) + "\n") 

