#!/usr/bin/env python

# script to align sequences using muscle
# Matthew J. Neave 4.2.2015

import sys
from Bio.Align.Applications import MuscleCommandline

input_handle = sys.argv[1]
output_handle = sys.argv[2]
muscle_exe = r"/home/neave/software/arb/bin/muscle"

cline = MuscleCommandline(muscle_exe, input=input_handle, out=output_handle, clw=True)

stdout, stderr = cline()



