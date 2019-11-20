#!/usr/bin/python3

def store_sraRunInfo(csvFile):
	import csv
	dic = {}
	f = open(csvFile)
	for row in csv.reader(f, delimiter = ','):
		if len(row) == 0 or row[0] == 'Run' or row[0] == '': continue
		srrID = row[0]
		l = int(row[6])
		sample = row[29]
		dic[sample] = [srrID, l]
	return dic

def main():
	import sys
	if len(sys.argv) != 3:
		sys.exit('python3 %s <all.SraRunInfo.csv> <sample_name.tissue.sex.tab.add.format>' % (sys.argv[0]))
	
	csvFile = sys.argv[1]
	tabFile = sys.argv[2]

	dic = store_sraRunInfo(csvFile)
	
	import csv
	f = open(tabFile)
	for row in csv.reader(f, delimiter = '\t'):
		srrID, l = dic[row[0]]
		print('%s\t%s\t%s\t%s\t%i\t%s' % (srrID, row[1], row[2], row[3], l, row[4]))

if __name__ == '__main__':
	main()

