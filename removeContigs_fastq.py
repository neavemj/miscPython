#!/usr/bin/env python

# script to remove sequences from fastq file below a certain length
# wrote with nanopore data in mind
# Matthew J. Neave 19.04.18

import sys
from Bio.SeqIO.QualityIO import FastqGeneralIterator # requires biopython

reads_fl = sys.argv[1]
required_length = int(sys.argv[2])
output = open(sys.argv[3], "w")

for title, seq, qual in FastqGeneralIterator(open(reads_fl)):
    if len(seq) > required_length:
        output.write("@%s\n%s\n+\n%s\n" % (title, seq, qual))
