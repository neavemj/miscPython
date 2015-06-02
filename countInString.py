#!/usr/bin/python

# count substring within DNA sequence file
# first input is file, second is substring, eg A.

import sys

total = 0


for line in open(sys.argv[1]):
	if line[0] != '>':  
		N = line.count(sys.argv[2])
		total = total + N
		
print 'total', sys.argv[2],':', total
