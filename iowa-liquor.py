import csv

f = open('iowa-liquor-sample.csv','r')
counter = 0
#with open('iowa-liquor-sample.csv',rb) as file:
for line in f:
	if line.lower().find('single malt scotch')>=0:
		counter += 1
print counter
