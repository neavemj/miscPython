#!/usr/bin/env python

# quick script to add ORFs to the XLOC numbers from cufflinks
# then can read into R for count heatmap
# Matthew J. Neave 27.11.15

import sys

count_data = open(sys.argv[1])      # genes.read_group_tracking
id_data = open(sys.argv[2])         # isoforms.fpkm_tracking //changed//
out_file = open(sys.argv[3], "w")   # gene.Rdf.txt

# read through id file and grab out the orf that corresponds to the xloc number

id_dict = {}

for line in id_data:
    line = line.strip().split("\t")
    xloc = line[3]
    orf = line[2]
    id_dict[xloc] = orf

# now add orf to the correct row
# count is used to add header to first row

count = 0

for line in count_data:
    line = line.strip()
    if count == 0:
        out_file.write(line + "\t" + "ORF" + "\n")
        count += 1
    else:
        line_spl = line.split("\t")
        xloc_num = line_spl[0]
        out_file.write(line + "\t" + id_dict[xloc_num] + "\n")
