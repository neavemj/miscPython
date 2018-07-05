#!/usr/bin/env python

# the WSSV genome is circular
# thus, assemblies often start at different positions
# this is not ideal for alignments
# want to rearrange all genomes to start at VP10
# this is where the first WSSV genome started (AF369029)
# will achieve this by blasting the VP10 gene against the genome
# and rearranging from that

import sys
import argparse
import subprocess
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO

# use argparse to grab command line arguments

parser = argparse.ArgumentParser("take a newly assembled WSSV genome and re-arrange it so that it starts at the VP10 "
                                 "region\nnote: requires blast+ tools to be available on the command line\nnote: "
                                 "requires that biopython is installed in python\n")

parser.add_argument('-g', '--genome', type = str,
        nargs = 1, help = "fasta file with genome to be re-arranged")
parser.add_argument('-o', '--output', type = str,
        nargs = 1, help = "new name for the re-arranged genome")

if len(sys.argv) == 1:  # if no args are given
    parser.print_help(sys.stderr)
    sys.exit(1)

args = parser.parse_args()

# check required arguments are provided

if args.genome is None or args.output is None:
    print("\n~~~ required output is missing ~~~\n"
          "~~~ input genome and an output file name is required ~~~\n")
    parser.print_help(sys.stderr)
    sys.exit(1)

# check that blast is loaded

try:
    tmp = subprocess.call(["blastn", "-version"])
except OSError as e:
    if e.errno == os.errno.ENOENT:
        print("\nblastn could not be found: try 'module load blast+'\n")
        raise

# make a blast database from the genome

subprocess.call(["makeblastdb", "-dbtype", "nucl", "-in", args.genome[0]])

# create and write out a WSSV VP10 record

VP10_record = SeqRecord(Seq("tggatctttctttcactctttcggtcgtgtcggccatcctcgccatcactgctgtgattgctgtatttattgtgatttttaggtatcacaacactgtgaccaagaccatcgaaacccacacagacaatatcgagacaaacatggatgaaaacctccgcattcctgtgactgctgaggttggatcaggctacttcaagatgactgatgtgtcctttgacagcgacaccttgggcaaaatcaagatccgcaatggaaagtctgatgcacagatgaaggaagaagatgcggatcttgtcatcactcccgtggagggccgagcactcgaagtgactgtggggcagaatctcacctttgagggaacattcaaggtgtggaacaacacatcaagaaagatcaacatcactggtatgcagatggtgccaaagattaacccatcaaaggcctttgtcggtagctccaacacctcctccttcacccccgtctctattgatgaggatgaagttggcacctttgtgtgtggtaccacctttggcgcaccaattgcagctaccgccggtggaaatcttttcgacatgtacgtgcacgtcacctactctggcactgagaccgagtaaataaatcgtgcttttttatatagatagggaattttaatattacaa"
                            ), id="AAK77670.1_nucl", name="VP10", description="WSSV_VP10_ORF1")
SeqIO.write(VP10_record, "VP10_record.fasta", "fasta")

# now blast the VP10 gene against the WSSV genome

subprocess.call(["blastn", "-query", "VP10_record.fasta", "-db", args.genome[0], "-outfmt", "6"])






