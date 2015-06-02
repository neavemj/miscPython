#!/usr/bin/python

# NOTES ON THIS PROGRAM
#
"""
This program produces three files. The first is allGenbankSearch.fasta, which is a fasta file of ALL of the results for your GenBank Search.
The second file is newGenbankSearch.fasta, which is a fasta containing only the NEW GenBank entries since the last running of this program.
Note: DO NOT RUN this program more than once in a short time. This will erase all of your new entries and you will not be able to distinguish
between new and old entries.
The third file this creates is an empty text file only if this is the first time you run this program. This is an arbitrary file only needed to 
make the program run, but can be discarded.
"""

from Bio import Entrez
from Bio import SeqIO
Entrez.email = "edenmark@whoi.edu"
print
the_term = str(raw_input('Hello Matt, what would you like to search today?   '))
handle = Entrez.esearch(db="nucleotide", term=the_term, retmax='10000')
record = Entrez.read(handle)
search_dict = {}
n=0
num_hosts = 0.0
num_locs = 0.0
host_dict = {}
location_dict = {}
too_long_dict = {}
no_loc = 0.0
for study in record['IdList']:
	num_hosts+=1
	num_locs+=1
	#dict format: {accession#:[endo_species,host,location,sequence]}
	new_handle = Entrez.efetch(db='nucleotide', id=study, rettype= 'gb', retmode = 'genbank')
	genome=SeqIO.read(new_handle,'genbank')
	search_dict[genome.id] = []
	sequence = genome.seq
	if len(sequence) >8000:
		sequence = 'Sequence Too Long; Not 16S  '
		too_long_dict[genome.id] = 0
	search_dict[genome.id].append(sequence)
	
	prefile = Entrez.efetch(db='nucleotide', id=study, rettype= 'gb', retmode='csv')
	
	organism = 'NotFound'
	host = 'NotFound'
	location = 'NotFound'
	seen = False
	for each_line in prefile:
		each_line = each_line.lstrip().rstrip().rstrip('\n')
				
		if each_line[:8].upper() == 'ORGANISM' and seen !=True:
			organism = each_line[8:].lstrip().rstrip().lstrip('\t')
			seen = True
			
		if each_line[:5] == '/host':
			host = each_line[5:].lstrip().rstrip().lstrip('\t')
			host = host.lstrip('="').rstrip('"')
			if host not in host_dict:
				host_dict[host] = 1
			else:
				host_dict[host] +=1
			
		if each_line[:8].upper() == 'LOCATION' or each_line[:8] == '/country':
			location = each_line[8:].lstrip().rstrip().lstrip('="').rstrip('"')
			if location not in location_dict:
				location_dict[location] = 1
			else:
				location_dict[location] +=1
			
		
	search_dict[genome.id].append(organism)
	search_dict[genome.id].append(host)
	search_dict[genome.id].append(location)	
	
	n +=1
	print n
print 'HOST INFORMATION:'
for each_host in host_dict:
	percent = ((host_dict[each_host])/(float(num_hosts)))*100.0
	print 'Of all the hosts,', percent, '% were', each_host
print
print 'LOCATION INFORMATION:'	
for each_loc in location_dict:
	percent = ((location_dict[each_loc])/(float(num_locs)))*100.0
	no_loc+=percent
	print 'Of all locations,', percent, '% were in', each_loc
not_found= 100.0 - no_loc
print not_found, '% did not have a given location.'

#WRITE FILE
try:
	old_file = open('allGenbankSearch.fasta','r')
except IOError:
	temp_file = open('temp_file.txt','w')
	temp_file.close()
	old_file = open('temp_file.txt', 'r')
lookup_dict = {}
for each_line in old_file:
	if each_line[0] == '>':
		each_line = each_line.lstrip('>')
		if each_line[2] == '_':
			each_line = each_line.split('_')
			each_line = str(each_line[0]+'_'+each_line[1])
		else:
			each_line = each_line.split('_')
			each_line = str(each_line[0])
		lookup_dict[each_line] = 0
old_file.close()
	
output_file = open('allGenbankSearch.fasta', 'w')
for each_study in search_dict:
	if each_study not in too_long_dict:

		each_study = str(each_study)
		organism = str(search_dict[each_study][1])
		host=str(search_dict[each_study][2])
		location = str(search_dict[each_study][3])
		sequence = str(search_dict[each_study][0])
		output_file.write('>'+each_study+'_'+organism+'_'+host+'_'+location+'\n')
		output_file.write(sequence+'\n')
output_file.close()

new_file = open('newGenbankSearch.fasta', 'w')
for accession in search_dict:
	if accession not in lookup_dict:
		accession = str(accession)
		organism = str(search_dict[accession][1])
		host=str(search_dict[accession][2])
		location = str(search_dict[accession][3])
		sequence = str(search_dict[accession][0])
		new_file.write('>'+accession+'_'+organism+'_'+host+'_'+location+'\n')
		new_file.write(sequence+'\n')
new_file.close()

num_new = (len(search_dict) - len(lookup_dict))
print 'There are ', num_new, 'new studies since the previous program run.'


