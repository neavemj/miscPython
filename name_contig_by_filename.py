#!/usr/bin/env python

# simple script to rename a contig by its filename
# useful for single contig wssv genome assemblies
# which often have weird contig names
# Matthew J. Neave 12.07.2018

import sys

fasta = open(sys.argv[1])
file_name = sys.argv[1].rstrip(".fasta")
output = open(sys.argv[2], "w")


contig_count = 0

for line in fasta:
    if contig_count > 1:
        print("error there is more than one contig in this file\n"
              "doesn't make sense to rename this way")
        sys.exit(1)
    if line.startswith(">"):
        contig_count += 1
        output.write(">" + file_name + "\n")
    else:
        output.write(line)


    
