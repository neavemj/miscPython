#!/usr/bin/env python

## take blastx result and figure out if contig is virus or phage
## -outfmt '6 qseqid sseqid evalue pident length bitscore sgi sacc stitle'

# Matthew J. Neave 31.5.15

import sys
import re # to extract contig name from the prodigal string

blast_handle = open(sys.argv[1])
output = open(sys.argv[2], "w")
virus_output = open(sys.argv[3], "w")

contig_dict = {}
contig_list = []

for result in blast_handle:
    result = result.strip()
    cols = result.split()
    contig_parts = cols[0].split("_")
    contig = contig_parts[0]+ "_" + contig_parts[1]

    if contig not in contig_dict:
        contig_dict[contig] = {"virus" : 0, "phage" : 0, "other" : 0}
    if contig not in contig_list:
        contig_list.append(contig)

    species = result.split("[")[1].replace("]", "")
    if "virus" in species:
        contig_dict[contig]["virus"] += 1
    if "phage" in species:
        contig_dict[contig]["phage"] += 1
    else:
        contig_dict[contig]["other"] +=1

# use the sorted list to write results

for contig in contig_list:
    output.write(contig + "\t" + "virus" + "\t" +
            str(contig_dict[contig]["virus"]) + "\t" 
            + "phage" + "\t" + str(contig_dict[contig]["phage"]) + "\t"
            + "other" + "\t" + str(contig_dict[contig]["other"])+"\n")
    if contig_dict[contig]["virus"] > 0:
        virus_output.write(contig + "\n")
