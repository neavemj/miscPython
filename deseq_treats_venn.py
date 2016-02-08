#!/usr/bin/env python

# venn diagrams for deseq sig genes over carp treatments
# Matthew J. Neave 08.02.2016

import sys
import matplotlib.pyplot as plt
import matplotlib_venn as vn

acVmo = open(sys.argv[1])
peVmo = open(sys.argv[2])
reVmo = open(sys.argv[3])

def get_sig_set(fl):
    sig_set = set()
    for line in fl:
        line = line.strip()
        cols = line.split()
        gene = cols[0]
        sig_set.add(gene)
    return sig_set

acVmo_set = get_sig_set(acVmo)
peVmo_set = get_sig_set(peVmo)
reVmo_set = get_sig_set(reVmo)

v = vn.venn3([acVmo_set, peVmo_set, reVmo_set], ("acute", "persistent",
"reactivated"), alpha=0.5)
# just added this circles part to modify line properties 
c = vn.venn3_circles([acVmo_set, peVmo_set, reVmo_set])
for j in c: j.set_lw(1.0)

plt.show()

