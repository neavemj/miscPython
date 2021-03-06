#!/usr/bin/env python

# Matthew J Neave 26.04.2016 
# extract sequences using a grep pattern 
# input fasta first, grep pattern, then a name for the output

import sys
from Bio import SeqIO
import re

fasta_file = sys.argv[1]  # input fasta file
grep_pat = open(sys.argv[2]).readlines() # grep pattern
result_file = sys.argv[3] # output name

re_pat = [re.compile(pat.strip()) for pat in grep_pat]

#pat = re.compile(grep_pat)

count = 0
fasta_sequences = SeqIO.parse(open(fasta_file),'fasta')
end = False
with open(result_file, "w") as f:
    for seq in fasta_sequences:
        for pat in re_pat:
            if re.findall(pat, seq.id) or \
               re.findall(pat, seq.description):
                SeqIO.write([seq], f, "fasta")
                count += 1       # keep track of how many IDs were found so can report later

print("Saved {} records from {} to {}".format(count, fasta_file, result_file))

