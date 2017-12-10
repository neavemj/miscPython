#!/usr/bin/env python
# python 3

# Matthew J Neave 6.5.2014
# extract sequences using a list of IDs
# input fasta first, then seq IDs, then a name for the output

import sys
from Bio import SeqIO

fasta_file = sys.argv[1]  # input fasta file
number_file = sys.argv[2] # list of sequence IDs of interest
result_file = sys.argv[3] # output name

wanted = set()
with open(number_file) as f:
    for line in f:
        line = line.strip()
        if line != "":
            wanted.add(line)


count = 0
fasta_sequences = SeqIO.parse(open(fasta_file),'fasta')
end = False
with open(result_file, "w") as f:
    for seq in fasta_sequences:
        seq_id = seq.id.split(":")[0] # this bit is for weird Trinity headers
        if seq_id not in wanted: # opposite. for example, pulling out non-blasted sequences
        #if seq_id in wanted:
            SeqIO.write([seq], f, "fasta")
            count += 1       # keep track of how many IDs were found so can report later

print("Saved {} records from {} to {}".format(count, fasta_file, result_file))
if count < len(wanted):
    print("Warning: {} IDs not found in {}".format(len(wanted)-count, fasta_file))

