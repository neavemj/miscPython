#!/usr/bin/env python

## python script to take interproscan output and format for topGO input (R package for go analysis)
## 18.8.14

# takes an output file from interScanPro, then a name to prefix the gene name with ie. genome name

import sys

genes = {}

for line in open(sys.argv[1]):
	words = line.replace('|', ' ')
	words = words.split()
	goList = []
	
	for j in words:
		
		if words[0] in genes:
			if j not in genes[words[0]]:
				if words[0] != j:			
					genes[words[0]].append(j)
			else:
				continue
		else:
			if words[0] != j:
				genes[words[0]] = [j]
	

f = open('interToTopGo.output', 'w')

for j in genes:	
	out = str(sys.argv[2] + j + '\t' + ", ".join(genes[j]) + '\n')				
	f.write(out)
