#!/usr/bin/env python

# Merge annotation with fpkm tables
# 05.04.2016

import sys

# get files

annot_file = open(sys.argv[1])
fpkm_file = open(sys.argv[2])
output = open(sys.argv[3], "w")

# create annotation dictionary

annot_dict = {}

for line in annot_file:
    line = line.strip()
    cols = line.split("\t")
    contig_name = cols[0]
    annot = cols[1]
    if contig_name in annot_dict:
        # this will append any new annotations on the end with a comma
        annot = "," + annot
        annot_dict[contig_name] += annot 
    else:
        annot_dict[contig_name] = annot

# read through fpkm file and add annotations

for line in fpkm_file:
    line = line.strip()
    cols = line.split("\t")
    contig = cols[0]
    if contig in annot_dict:
        output.write(line + "\t" + annot_dict[contig] + "\n")
    else:
        output.write(line + "\tNone\n")


