#!/usr/bin/env python

# take fasta file and extract reads from F and R fastq file
# Matthew J. Neave 2.6.15

import sys
from Bio.SeqIO.QualityIO import FastqGeneralIterator # use this biopython module to deal with fastq files

fasta_handle = open(sys.argv[1])
fastq1_handle = open(sys.argv[2])
fastq2_handle = open(sys.argv[3])
fastq1_out = open(sys.argv[4], "w") 
fastq2_out = open(sys.argv[5], "w")

# make set of reads from fasta file

fasta_set = set()

for read in fasta_handle:
    read = read.strip()
    if read.startswith(">"):
        read = read.lstrip(">")
        fasta_set.add(read)

# scan fastq files and write matching reads

for title, seq, qual in FastqGeneralIterator(fastq1_handle):
    name = title.split()[0].lstrip("@")
    if name in fasta_set:
        fastq1_out.write("@%s\n%s\n+\n%s\n" % (title, seq, qual))

for title, seq, qual in FastqGeneralIterator(fastq2_handle):
    name = title.split()[0].lstrip("@")
    if name in fasta_set:
        fastq2_out.write("@%s\n%s\n+\n%s\n" % (title, seq, qual))
