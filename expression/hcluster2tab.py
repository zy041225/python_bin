#!/usr/bin/python3

def hcluster2tab(hcFile):
	f = open(hcFile)
	import csv
	import re
	pattern = re.compile(r'(\S+)_(\S+)')

	reader = csv.reader(f, delimiter = '\t')
	for row in reader:
		row[6] = row[6].rstrip(',')
		tmp = row[6].split(',')
		for i in tmp:
			match = pattern.match(i)
			id = match.group(1)
			spe = match.group(2)
			print('%s\t%s\t%s' % (id, spe, row[0]))


def main():
	import sys
	if len(sys.argv) != 2:
		sys.exit('python3 %s <hcluster>' % (sys.argv[0]))

	hcFile = sys.argv[1]
	hcluster2tab(hcFile)

if __name__ == '__main__':
	main()

