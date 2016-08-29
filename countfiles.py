#!/usr/bin/env python
# python 3 

# quick script to count number of individual files in given dir
# Matthew J. Neave 29.08.16

import os, sys

basedir = sys.argv[1]
num_files = 0

for path, dirs, files in os.walk(basedir):
    num_files += len(files)

print("number of files in {}:".format(os.path.abspath(basedir)), num_files)
