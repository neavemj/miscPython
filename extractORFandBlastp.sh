#!/bin/bash

## unix script - extract ORFs and blast them ##
# Matthew J Neave #

# to use files from the command line in shell script
# command: ./script.bash alpha beta gamma
# Variables: $1=='alpha'; $2=='beta'; $3=='gamma'
# so the first file listed after the ./extractORFandBlastp.sh is contained in the variable $1

# extract ORFs with prodigal, then clean up a bit with cut

prodigal -a temp.orfs.faa -i $1 -m -o temp.txt -p meta -q
cut -f1 -d " " temp.orfs.faa > final.orfs.faa

# blast the extracted ORFs

blastp -query final.orfs.faa -db /home/share/db/nr_Jul14/nr -evalue 1e-3 -num_threads 8 -max_target_seqs 5 -outfmt "7 pident seqid stitle" -out final.orfs.faa.blastp

echo 'final.orfs.faa.blastp contains the blast results' 
echo 'final.orfs.faa contains amino acid sequences of the ORFs'


