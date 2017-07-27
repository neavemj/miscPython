#!/usr/bin/env python

# script to grab mate after subsetting somehow
# Matthew J. Neave 27.7.2017 <matthewjneave1@gmail.com>

# library imports

import sys
import argparse
from Bio.SeqIO.QualityIO import FastqGeneralIterator # requires Biopython

# use argparse to grab command line arguments

parser = argparse.ArgumentParser("get opposite read pair from subsetted file")

parser.add_argument('subset_reads', type = str,
        nargs = "?", help = "fastq file containing subsetted reads")
parser.add_argument('opposite_reads', type = str,
        nargs = "?", help = "fastq file containing opposite reads to extract")
parser.add_argument('output', type = str,
        nargs = "?", help = "name for the output file")

args = parser.parse_args()
output_handle = open(args.output, "w")

print "Scanning subsetted file and building list of names..."
subset_ids = set()
for title, seq, qual in FastqGeneralIterator(open(args.subset_reads)):
    subset_ids.add(title.split()[0])

print "Processing opposite file"

for title, seq, qual in FastqGeneralIterator(open(args.opposite_reads)):
    name = title.split()[0]
    if name in subset_ids:
        # paired reads
        subset_ids.remove(name) # saves a little memory
        output_handle.write("@%s\n%s\n+\n%s\n" % (title, seq, qual))
output_handle.close()

print "done"
