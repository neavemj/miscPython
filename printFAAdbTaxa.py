#!/usr/bin/env python

# check which viruses are most abundant in the NCBI viral DB
# Matthew J. Neave 10.6.15

import sys

db = open(sys.argv[1])
db_dict = {}

for line in db:
    line = line.strip()
    if line.startswith(">"):
        species = line.split("[")[1].strip("]")
        db_dict[species] = db_dict.get(species, 1) + 1

sorted_db = sorted(db_dict, key=db_dict.get, reverse=True)

for key in sorted_db[:50]:
    print key, db_dict[key]
