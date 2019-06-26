#!/usr/bin/env python

"""
Take the gff output from Prokka and create
files suitable for circos, including the
forward and reverse gene locations,
plus a chr file of the size of each chromosome.
Requires the sequence to be appended at the
end of the gff file, which is the default
for prokka
"""

from Bio import SeqIO
import argparse


parser = argparse.ArgumentParser("""
    Take the gff output from Prokka and create
    files suitable for circos, including the
    forward and reverse gene locations,
    plus a chr file of the size of each chromosome.
    Requires the sequence to be appended at the
    end of the gff file, which is the default
    for prokka.
    Output will be named according to chr name.
""")

parser.add_argument('-g', '--gff', type = str,
        help = "gff file as output by prokka")

if len(sys.argv) == 1:  # if no args are given
    parser.print_help(sys.stderr)
    sys.exit(1)

args = parser.parse_args()

# check required arguments are provided

if args.gff is None:
    print("*** error: required argument is missing"
          "*** error: gff file from prokka is required")
    parser.print_help(sys.stderr)
    sys.exit(1)

# read through gff and extract required information
















