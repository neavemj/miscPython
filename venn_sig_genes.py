#!/usr/bin/env python

# Make a venn diagram of sig genes across treatments
# Matthew J. Neave 31.1.17
# will grab the first column of a table as the gene names
# can give either 2 or 3 files 

import sys
import matplotlib.pyplot as plt
import matplotlib_venn as vn

# get sets of sig genes

def create_sig_set(fl):
    fl_open = open(fl)
    gene_set = set()
    for line in fl_open:
        line = line.strip()
        cols = line.split(" ")
        gene = cols[0]
        gene_set.add(gene)
    return gene_set

set_list = []
for fl in sys.argv[1:]:
    new_set = create_sig_set(fl)
    set_list.append(new_set)

# now create venn diagrams of these sets
text_names = [name.split(".")[0] for name in sys.argv[1:]]
if len(set_list) == 2:
    vn.venn2(set_list, text_names)
    c = vn.venn2_circles(set_list, linestyle='dashed')
if len(set_list) == 3:
    vn.venn3(set_list, text_names)
    c = vn.venn3_circles(set_list, linestyle='dashed')
for circ in c:
    circ.set_lw(1.0)
plt.show()

