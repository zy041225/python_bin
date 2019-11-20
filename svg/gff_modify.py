#!/usr/bin/env python3

def main():
	import sys
	if len(sys.argv) != 4:
		sys.exit('python3 %s <gff> <gene_len> <intergenic len>' % (sys.argv[0]))

	inFile = sys.argv[1]
	gLen = int(sys.argv[2])
	iLen = int(sys.argv[3])

	last_chr = ''
	last_bg = 1

	

if __name__ == '__main__':
	main()

