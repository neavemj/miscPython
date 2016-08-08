#!/usr/bin/env python

# add go annotations to uniprot IDs 
# use mapping file for translations
# Matthew J. Neave 09.08.16

import sys

annot_fl = open(sys.argv[1])
map_fl = open(sys.argv[2])
output = open(sys.argv[3], "w")

# extract information from uniprot => GO mapping file
# store results in dictionary for later
# sometimes there is more than 1 GO term, make a list for these

uniGO_dict = {}

for line in map_fl:
    if not line.startswith("!"):
        line = line.strip()
        cols = line.split()
        uniprot_id = cols[1]
        GO_id = cols[3]
        if uniprot_id in uniGO_dict:
            uniGO_dict[uniprot_id].append(GO_id)
        else:
            uniGO_dict[uniprot_id] = [GO_id]

# now loop through annotation file
# add GO terms for each uniprot id if they are present

for line in annot_fl:
    line = line.strip()
    cols = line.split()
    uniprot_id = cols[1]
    if uniprot_id in uniGO_dict:
        output.write(line + "\t" + ",".join(uniGO_dict[uniprot_id]) + "\n")
    else:
        output.write(line + "\t\n")
