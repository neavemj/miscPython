#!/usr/bin/env python

# reverse complement DNA sequence
# Matthew J Neave 6.6.14

import sys
from Bio import SeqIO
from Bio import Seq
from Bio.Alphabet import IUPAC

fasta_file = sys.argv[1]  # fasta file to reverse complement
output = sys.argv[2]	# name of output file

fasta_sequences = SeqIO.parse(fasta_file,'fasta',alphabet=IUPAC.unambiguous_dna)

with open(output, "w") as f:
	for j in fasta_sequences:
		RCj = j.reverse_complement(id=True, name=True, description=True)		
		SeqIO.write(RCj, f, "fasta")
		
f.close()