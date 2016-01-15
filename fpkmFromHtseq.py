#!/usr/bin/env python

# take counts from HTseq, plus gff file and compute fpkm
# Matthew J. Neave

import sys

counts = open(sys.argv[1])
gff = open(sys.argv[2])
total_reads = int(sys.argv[3])
out = open(sys.argv[4], "w")

# get name and gene lengths from gff
# if multiple exons, sum to get length

gff_dict = {}

for line in gff:
    line = line.strip()
    cols = line.split("\t")
    region = cols[2]
    start = int(cols[3])
    end = int(cols[4])
    length = end - start
    orf = cols[8].replace("Parent=", "")
    if orf in gff_dict:
        gff_dict[orf] += length
    else:
        gff_dict[orf] = length

# read through counts from HTseq and calculate fpkm

for line in counts:
    line = line.strip()
    cols = line.split("\t")
    orf = cols[0]
    count = int(cols[1])
    try:
        fpkm = float(10**9 * count) / float(total_reads * gff_dict[orf])
        out.write(line + "\t" + str(fpkm) + "\n")
    except:
        print "key not found:", orf

