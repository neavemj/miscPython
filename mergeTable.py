#!/usr/bin/env python
# python 3

# merge individual outputs into one table
# assumes generic format of two columns (gene and count)
# Matthew J. Neave 07.11.17

import sys

output = sys.argv[1]

# Keep track of row names in case some files don't have all genes
# make a dict of dicts to keep track of everything

count_dict = {}
gene_list = []
fl_list = []
fl_count = 0

for fl_name in sys.argv[2:]:
    name = fl_name.split(".")[0]
    fl_list.append(name)
    fl_count += 1
    count_dict[name] = {}
    with open(fl_name) as f:
        for line in f:
            line = line.strip()
            cols = line.split("\t")
            gene = cols[0]
            if gene.startswith("_"):
                continue
            if gene not in gene_list:
                gene_list.append(gene)
            count = cols[1]
            count_dict[name][gene] = count

# now write the results out to matrix file

with open(output, "w") as w:
    # write out header line first
    w.write("\t" + "\t".join(fl_list) + "\n")
    # now get counts for each gene
    for gene in gene_list:
        w.write(gene + "\t")
        tmp_count_list = []
        for fl in fl_list:
            if gene in count_dict[fl]:
                tmp_count_list.append(count_dict[fl][gene])
            else:
                tmp_count_list.append("0")
        w.write("\t".join(tmp_count_list) + "\n")


