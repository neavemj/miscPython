#!/bin/bash

## unix script - check for essential genes script 2.4.14 ##
# Matthew J Neave #

# to use files from the command line in shell script
# command: ./script.bash alpha beta gamma
# Variables: $1=='alpha'; $2=='beta'; $3=='gamma'

# so the first file listed after the ./essentialGenes.sh is contained in the variable $1

metrics $1

# extract ORFs

prodigal -a temp.orfs.faa -i $1 -m -o temp.txt -p meta -q
cut -f1 -d " " temp.orfs.faa > final.orfs.faa

# search for essential genes
# tail -n+4 takes the end of the file except for the first 4 rows
# head -n-10 takes the top of the input except the final 10 rows
# cut -f4 -d " " takes only the 4th column 

hmmsearch --tblout temp.hmm.orfs.txt --cut_tc --notextw /home/neave/software/multi-metagenome/R.data.generation/essential.hmm final.orfs.faa
tail -n+4 temp.hmm.orfs.txt | head -n-10 | sed 's/ * / /g' | cut -f4 -d " " > final.orfs.hmm.id.txt

echo 'essential genes:' > essentialGenes.summary
grep -c $ final.orfs.hmm.id.txt >> essentialGenes.summary
echo 'unique genes:' >> essentialGenes.summary
uniq final.orfs.hmm.id.txt | grep -c $ >> essentialGenes.summary

echo 'essential genes:'
grep -c $ final.orfs.hmm.id.txt
echo 'unique genes:'
uniq final.orfs.hmm.id.txt | grep -c $ 
echo 'final.orfs.faa contains the ORF amino acid sequence' 
echo 'final.orfs.hmm.id.txt contains a list of the essential genes'



