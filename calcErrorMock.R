#!/usr/bin/env Rscript

## calculates the error rate based on a mock community ##
# based on the Schloss Miseq SOP #
# Matthew J. Neave 7.11.14 #

# grab the file names from the command line

file_handles <- commandArgs(TRUE)
errorSummary_handle <- file_handles[1]
count_handle <- file_handles[2]

# do the SOP calculations

s <- read.table(file=errorSummary_handle, header=T)
ct <- read.table(file=count_handle, header=T)
rownames(s) <- s[,1]
rownames(ct) <- ct[,1]
no.chim <- s$numparents==1
s.good <- s[no.chim,]
query <- rownames(s.good)
ct.good <- ct[as.character(query),]

# need to get mock name incase it's unique - get it from the count file

mock_name <- names(ct.good)[3]
print("Percentage Error Rate:", quote=F)

# now use the mock variable 
# can't use $ notation in this case - have to subset with square brackets

sum(ct.good[,mock_name] * s.good$mismatches)/sum(ct.good[,mock_name] * s.good$total)
