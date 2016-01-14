#!/usr/bin/env python

# quick find file script

import os, sys, re

name = sys.argv[1]

for path, dirs, files in os.walk("."):
    for fl in files:
        if re.findall(name, fl):
            full_path = os.path.join(path, fl)
            print os.path.abspath(full_path)
