#!/bin/bash

## quick UNIX script to clean up blast results from extractORFsBlastp.sh 8.4.14 ##
# have to do this because of the X11 window time out problem #

MEGAN +g -x "import blastfile= final.orfs.faa.blast.xml meganfile=temp.rma;recompute toppercent=5;recompute minsupport=1;update;collapse rank=Species;update;select nodes=all;export what=CSV format=readname_taxonpath separator=tab file=final.orfs.blast.tax.txt;update;close"
