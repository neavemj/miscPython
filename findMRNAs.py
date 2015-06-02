#!/usr/bin/env python

# Matthew J Neave 6.5.2014
# extract sequences that didn't match rRNA 
# input fasta first, then IDs with rRNA match, then a name for the output

import sys
from Bio import SeqIO

fasta_file = sys.argv[1]  # input fasta file
rRNA_file = sys.argv[2] # list of IDs that matched rRNA
result_file = sys.argv[3] # output name

ribosomal = set()
with open(rRNA_file) as f:
    for line in f:
        line = line.strip()
        if line != "":
            ribosomal.add(line)


count = 0 
fasta_sequences = SeqIO.parse(open(fasta_file),'fasta')
end = False
with open(result_file, "w") as f:
    for seq in fasta_sequences:
        if seq.id not in ribosomal:
            SeqIO.write([seq], f, "fasta")
            count += 1       # keep track of how many IDs were found so can report later
        
print "Saved %i records from %s to %s" % (count, fasta_file, result_file)



