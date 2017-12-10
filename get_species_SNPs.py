#!/usr/bin/env python
# python 3

# take kissplice output and get 'species-specific' SNPs
# Matthew J. Neave 06.12.2017

######################################
# the variables below can be changed..
SNP_file = "head_n70_mainOutput.txt"
output = open("species_SNPs.txt", "w")
minimum_reads = 10
######################################

def clean_counts(input_col):
    # returns list of integers of actual read counts
    # the sample name, underscore and pipe char are removed
    sample_counts = input_col.split("|")
    counts = [int(c.split("_")[1]) for c in sample_counts]
    return(counts)

with open(SNP_file) as fl:
    # skip header
    next(fl)
    # now loop through lines
    for line in fl:
        line_s = line.strip()
        cols = line_s.split("\t")
        allele_freq = cols[13]
        counts1 = clean_counts(cols[14])
        counts2 = clean_counts(cols[15])
        # filter out species-specific SNPs for the first case
        if allele_freq == "100.0|100.0|100.0|100.0|0.0|0.0|0.0|0.0" \
        and all(c >= minimum_reads for c in counts1[:4]) \
        and all(i >= minimum_reads for i in counts2[4:]):
            output.write(line)

        # filter out species-specific SNPs for the vice versa case
        elif allele_freq == "0.0|0.0|0.0|0.0|100.0|100.0|100.0|100.0" \
        and all(c >= minimum_reads for c in counts1[4:]) \
        and all(i >= minimum_reads for i in counts2[:4]):
            output.write(line)
