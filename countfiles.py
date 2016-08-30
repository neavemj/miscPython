#!/usr/bin/env python
# python 3 

# quick script to count number of individual files in given dir
# Matthew J. Neave 29.08.16

import os, sys

basedir = sys.argv[1]
num_files = 0
num_dirs = 0

for path, dirs, files in os.walk(basedir):
    num_files += len(files)
    num_dirs += len(dirs)

print(num_files, "files,", num_dirs, "dirs in {}".format(os.path.abspath(basedir)))
