#!/usr/bin/env python

## script to get which organisms are most abundant in blastx results
## -outfmt '6 qseqid sseqid evalue pident length bitscore sgi sacc stitle'

# Matthew J. Neave 27.5.15

import sys
import pylab as pl
import numpy as np

blast_handle = open(sys.argv[1])
output = open(sys.argv[2], "w")

blastDict = {}

for result in blast_handle:
    result = result.strip()
    cols = result.split()
    try:
        species = result.split("[")[1].replace("]", "")
        blastDict[species] = blastDict.get(species,0) + 1
    except:
        pass


# sort results and write to file
sorted_dict = sorted(blastDict.items(), key = lambda x:x[1], reverse=True)
for record in sorted_dict:
    output.write("\t".join(map(str, record)) + "\n")


# plotting with matplotlib
if 1 == 2:
    sortedList = zip(*sorted_dict)
    x_axis = np.arange(len(sortedList[1]))
    pl.bar(x_axis, sortedList[1], align="center")
    pl.xticks(x_axis, sortedList[0], rotation="vertical")
    xmax = max(x_axis)
    pl.xlim(0, xmax)
    pl.show()
