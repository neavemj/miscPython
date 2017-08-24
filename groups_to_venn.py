#!/usr/bin/env python
# python 3

# takes groups.txt from orthoMCL run and produces venn diagram

import sys
import os
import matplotlib.pyplot as plt
import matplotlib_venn as vn

# first grab full set of proteins from each genome 

full_dict = {}
genome_names = []

for j in sys.argv[2:]:
    base = os.path.basename(j)
    name = base.split(".")[0] 
    full_dict[name] = set()
    genome_names.append(name)
    f_handle = open(j)
    for line in f_handle:
        if line.startswith(">"):
            header = line.strip().lstrip(">")
            full_dict[name].add(header)

# now go through groups file and get homologues

all_homologues_set = set()
homologues_dict = {}

for line in open(sys.argv[1]):
    line = line.strip()
    cols = line.split()
    cluster = cols[0].lstrip(":")
    tmp_set = set()
    for protein in cols[1:]:
        all_homologues_set.add(protein) 
        tmp_set.add(protein) 
        for genome in genome_names:
            if protein.startswith(genome):
                if genome in homologues_dict:
                    homologues_dict[genome].add(cluster)
                else:
                    homologues_dict[genome] = set(cluster)

final_sets = []

for name in genome_names:
    non_homol = full_dict[name] - all_homologues_set
    final_sets.append(non_homol.union(homologues_dict[name]))

vn.venn3(final_sets, genome_names)
plt.show()
