#!/usr/bin/env python

# simple script to rename a contig by its filename
# useful for single contig wssv genome assemblies
# which often have weird contig names
# Matthew J. Neave 12.07.2018

import sys, os

fasta = open(sys.argv[1])
file_name = os.path.basename(sys.argv[1]).rstrip(".fasta")
output = open(sys.argv[2], "w")

contig_count = 0

for line in fasta:
    if line.startswith(">"):
        contig_count += 1
        output.write(">" + file_name + "_" + str(contig_count) + "\n")
    else:
        output.write(line)


    
