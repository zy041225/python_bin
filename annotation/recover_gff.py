#!/usr/bin/env python3

import sys

def main():
	if len(sys.argv) != 2:
		sys.exit('python3 %s <tmp.gff>' % (sys.argv[0]))

	gffFile = sys.argv[1]

	with open(gffFile) as f:
		for line in f:
			line = line.rstrip()
			tmp = line.split('\t')
			info = tmp[0].split('##')
			tmp[0] = info[1]
			tmp[3] = str(int(tmp[3])+int(info[2])-1)
			tmp[4] = str(int(tmp[4])+int(info[2])-1)
			out = '\t'.join(tmp)
			print('%s' % (out))

if __name__ == '__main__':
	main()

