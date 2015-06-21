#!/usr/bin/env python

## take blastx result and figure out given species abundance
## -outfmt '6 qseqid sseqid evalue pident length bitscore sgi sacc stitle'

# Matthew J. Neave 21.6.15

import sys

blast_handle = open(sys.argv[1])
output = open(sys.argv[2], "w")
search = sys.argv[3]

contig_dict = {}
contig_list = []

for result in blast_handle:
    result = result.strip()
    cols = result.split()
    contig_parts = cols[0].split("_")
    contig = contig_parts[0]+ "_" + contig_parts[1]

    if contig not in contig_dict:
        contig_dict[contig] = {search : 0, "other" : 0}
    if contig not in contig_list:
        contig_list.append(contig)
    
    try:
        species = result.split("[")[1].replace("]", "")
    except:
        print "unable to extract species from:", result
    
    if search in species:
        contig_dict[contig][search] += 1
    else:
        contig_dict[contig]["other"] +=1

# use the sorted list to write results

for contig in contig_list:
    output.write(contig + "\t" + search + "\t" +
            str(contig_dict[contig][search]) + "\t" 
            + "other" + "\t" + str(contig_dict[contig]["other"])+"\n")
