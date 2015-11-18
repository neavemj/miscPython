#!/usr/bin/env python

# 6.11.15 create combined MED matrix plus taxonomy table from mothur
# similar to file created with full mothur pipeline

import sys

# open files

matrix = open(sys.argv[1])
tax = open(sys.argv[2])
out = open(sys.argv[3], "w")

# create matrix list so can transpose using zip

matrix_list = []

for line in matrix:
    line = line.strip().split()
    matrix_list.append(line)

transposed_matrix_list = zip(*matrix_list)

# create dict from this list for easier referencing later

med_dict = {}

for node in transposed_matrix_list:
    med_dict[node[0]] = node[1:]

# read in tax file and output new format

for line in tax:
    line = line.strip().split()
    med_node = line[0]
    tax_string = line[2:]
    cat_tax_string = ";".join(tax_string)
    if med_node in med_dict:
        med_tax = med_dict[med_node]
        out.write(med_node + "\t" + cat_tax_string + "\t" + "\t".join(med_tax) + "\n")
    elif med_node == "MEDnode":
        out.write(med_node + "\t" + cat_tax_string + "\t" +
                "\t".join(med_dict["samples"]) + "\n")
    else:
        print "key error", med_node
