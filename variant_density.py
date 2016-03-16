#!/usr/bin/env python

# get variant density per gene of khv genome
# Matthew J. Neave

import sys

gene_file = open(sys.argv[1])
variant_file = open(sys.argv[2])
output = open(sys.argv[3], "w")

# go through variants and check if they're within a genes coordinates

gene_dict = {}
gene_count = 0
variant_list = [x for x in variant_file]

for gene in gene_file:
    gene_count += 1
    cols = gene.strip().split("\t")
    start = int(cols[1])
    end = int(cols[2])
    gene_dict[gene_count] = {"start": start, "end": end}
    gene_range = range(start, end)
    for snp in variant_list:
        snp = int(snp.strip().split("\t")[1])
        if snp in gene_range:
            if "snps" in gene_dict[gene_count]:
                gene_dict[gene_count]["snps"] += 1
            else:
                gene_dict[gene_count]["snps"] = 1 

# now write snp counts to file for circos

for record in gene_dict:
    start = str(gene_dict[record]["start"])
    end = str(gene_dict[record]["end"])
    length = gene_dict[record]["end"] - gene_dict[record]["start"]
    if "snps" in gene_dict[record]:
        snps = str((float(gene_dict[record]["snps"]) / float(length)) * 100)
    else:
        snps = "0"
    output.write("khv1\t" + start + "\t" + end + "\t" + snps + "\n") 
