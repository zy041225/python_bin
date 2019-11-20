#!/usr/bin/env python3

def main():
	import sys
	from Bio import AlignIO
	import re

	if len(sys.argv) != 3:
		sys.exit('python3 %s <xmfa> <region>'  % (sys.argv[0]))

	inFile = sys.argv[1]
	region = sys.argv[2]

	match = re.match(r'(\w+):(\d+)-(\d+)', region)
	scaf = match.group(1)
	bg = int(match.group(2))
	ed = int(match.group(3))

	f = AlignIO.parse(inFile, 'mauve')
	for aln in f:
		print(aln)	

if __name__ == '__main__':
	main()

