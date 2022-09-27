#!/usr/bin/env python

'''
Compiled by Felix Francis (felixfrancier@gmail.com)
Description:    Parse multiple sequence alignment out put files and calculate Shannon's entropy for each column of the alignment.
                Shannon's entropy equation (latex format):
                
                H=-\sum_{i=1}^{M} P_i\,log_2\,P_i
                
                Entropy is a measure of the uncertainty of a probability distribution (p1, ..... , pM)
                https://stepic.org/lesson/Scoring-Motifs-157/step/7?course=Bioinformatics-Algorithms&unit=436
                
                Where, Pi is the fraction of nuleotide bases of nuleotide base type i, and M is the number of nuleotide base types (A, T, G or C)
                
                H ranges from 0 (only one base/residue in present at that position) to 4.322 (all 20 residues are equally represented in that position).
                Typically, positions with H >2.0 are considerered variable, whereas those with H < 2 are consider conserved.
                Highly conserved positions are those with H <1.0 (Litwin and Jores, 1992). A minimum number of sequences is however required (~100)
                for H to describe the diversity of a protein family.
               
'''

import sys
#import pandas as pd
from Bio import AlignIO
#from numpy.random import randn

# read in muscle aligned file
align_clustal = AlignIO.read(sys.argv[1], "fasta")

output = open(sys.argv[2], "w")

##################################################################
# Function to calcuate the Shannon's entropy per alignment column
# H=-\sum_{i=1}^{M} P_i\,log_2\,P_i (http://imed.med.ucm.es/Tools/svs_help.html)
# Gaps and N's are included in the calculation
##################################################################
def shannon_entropy(list_input):
    import math
    unique_base = set(list_input)                           # Get only the unique bases in a column
    #unique_base = unique_base.discard("-")
    M   =  len(list_input)
    entropy_list = []
    # Number of residues in column
    for base in unique_base:
        n_i = list_input.count(base)                        # Number of residues of type i                   
        P_i = n_i/float(M)                                  # n_i(Number of residues of type i) / M(Number of residues in column)
        entropy_i = P_i*(math.log(P_i,2))
        entropy_list.append(entropy_i)
    sh_entropy = -(sum(entropy_list))
    #print sh_entropy
    return sh_entropy


##################################################################
# Function to calculate Shannon's entropy per alignment column for the whole MSA
##################################################################

def shannon_entropy_list_msa(alignment_file):
    shannon_entropy_list = []
    for col_no in range(len(list(alignment_file[0]))):
        list_input = list(alignment_file[:, col_no])
        shannon_entropy_list.append(shannon_entropy(list_input))
    return shannon_entropy_list


entropy_list = shannon_entropy_list_msa(align_clustal)

# write out entropy_list with positions

for index, entropy in enumerate(entropy_list):
    output.write(str(index+1) + "\t" + str(entropy) + "\n")


