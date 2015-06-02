#!/usr/bin/env python

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
        if seq.id in wanted:
            SeqIO.write([seq], f, "fasta")
            count += 1       # keep track of how many IDs were found so can report later
        
print "Saved %i records from %s to %s" % (count, fasta_file, result_file)
if count < len(wanted):
    print "Warning %i IDs not found in %s" % (len(wanted)-count, fasta_file)

