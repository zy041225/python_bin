#!/usr/bin/python3

def store(dic, csvFile, sample):
	import csv
	f = open(csvFile)
	reader = csv.reader(f, delimiter = ',')
	next(reader, None)
	for row in reader:
		dic[row[0]][sample] = row[1]
	return dic

def main():
	import sys
	if len(sys.argv) < 2:
		sys.exit('python3 %s <csv.tab>' % (sys.argv[0]))

	tabFile = sys.argv[1]

	from collections import defaultdict
	dic = defaultdict(dict)
	samDic = {}

	f = open(tabFile)
	for line in f:
		line = line.rstrip()
		tmp = line.split('\t')
		sample, csvFile = tmp[:2]
		samDic[sample] = 1
		dic = store(dic, csvFile, sample)
	
	h = '\t'.join([sample for sample in sorted(samDic)])
	print(h)
	for gene in sorted(dic):
		out = gene + '\t' + '\t'.join([dic[gene][sample] for sample in sorted(dic[gene])])
		print(out)

if __name__ == '__main__':
	main()

