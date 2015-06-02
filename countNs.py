#!/usr/bin/python

import sys

totalN = 0
totaln = 0

for line in open(sys.argv[1]):
	if line[0] != '>':  
		N = line.count('N')
		n = line.count('n')
		totalN = totalN + N
		totaln = totaln + n
		
print 'total Ns:', totalN
print 'total ns:', totaln
