#!/usr/bin/env python

# quick find file script

import os, sys

name = sys.argv[1]

for path, dirs, files in os.walk("."):
    if name in files:
        full_path = os.path.join(path, name)
        print os.path.abspath(full_path)
