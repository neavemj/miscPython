import numpy
import pylab

your_file = str(raw_input('Enter file name:   '))
num_bins = int(raw_input('How many bins do you want?   '))
new_file = open(your_file, 'r')
len_dict = {}
len_dict['A. 0-50']= -1
len_dict['B. 51-100']=0
len_dict['C. 101-150']=0
len_dict['D. 151-200']=0
len_dict['E. 201-250']=0
len_dict['F. 251-300']=0
len_dict['G. 301-350']=0
len_dict['H. 351-400']=0
len_dict['I. 401-450']=0
len_dict['J. 451-500']=0
len_dict['K. 501-550']=0
len_dict['L. Over 500']=0

total = []
n=0
for each_line in new_file:
	each_line.rstrip('\n').lstrip('\n')
	if each_line[0] == '>':
		total.append(n)
		if n <= 50:
			len_dict['A. 0-50'] +=1
		elif n<=100:
			len_dict['B. 51-100'] +=1
		elif n<=150:
			len_dict['C. 101-150'] +=1
		elif n<=200:
			len_dict['D. 151-200'] +=1
		elif n<=250:
			len_dict['E. 201-250'] +=1
		elif n<=300:
			len_dict['F. 251-300'] +=1
		elif n<=350:
			len_dict['G. 301-350'] +=1
		elif n<=400:
			len_dict['H. 351-400'] +=1	
		elif n<=450:
			len_dict['I. 401-450'] +=1
		elif n<=500:
			len_dict['J. 451-500'] +=1
		elif n<550:
			len_dict['K. 501-550'] +=1
		elif n>550:	
			len_dict['L. Over 500'] +=1		
		n=0
		end = False
	else:
		for each_char in each_line:
						
			n+=1
		
			
name_list = []
for name in len_dict:
	name_list.append(name)

name_list = sorted(name_list)
	
for name in name_list:
	print name, ':', len_dict[name]
avg = (float(sum(total))/(len(total)))
print 'Average: ', avg

ylist = []
for name in name_list:
	ylist.append(len_dict[name])


pylab.hist(total,num_bins, (0,max(total)))
pylab.title('Length of Reads')
pylab.xlabel('number of nucleotides')
pylab.ylabel('number of sequences')
pylab.show()

