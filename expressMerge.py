#!/usr/bin/env python

# script to take column 8 from express table and merge with other results
# run this first: cut -f 2,8 results.xprs > sampleCounts 
# Matthew J. Neave 26.3.15

import sys

output_handle = open("combinedExpress.txt", "w")


fileDict = {}

for arg in sys.argv[1:]:
	fileDict[arg] = {}
	for line in open(arg):
		cols = line.strip().split('\t')
		gene = cols[0]
		count = cols[1]
		fileDict[arg][gene] = count

sampleList = [x for x in fileDict]
sampleList.sort()

for key in fileDict:
	output_handle.write("gene" + "\t" + "\t".join(sampleList) + "\n")
	for gene in fileDict[key]:
		output_handle.write(gene + "\t")
		for sample in sampleList:
			output_handle.write(fileDict[sample][gene] + "\t")
		output_handle.write("\n")
	break
