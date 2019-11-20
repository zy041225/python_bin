#!/usr/bin/env python3

def store(lstFile):
	dic = {}
	with open(lstFile) as f:
		for line in f:
			line = line.rstrip()
			tmp = line.split('\t')
			id = tmp[0]
			name = tmp[1]
			dic[id] = name
	return dic

def main():
	import sys
	import re

	if len(sys.argv) != 3:
		sys.exit('python3 %s <ID_name.lst> <gff>' % (sys.argv[0]))
	
	lstFile = sys.argv[1]
	gffFile = sys.argv[2]

	dic = store(lstFile)

	with open(gffFile) as f:
		for line in f:
			line = line.rstrip()
			tmp = line.split('\t')
			info = tmp[8].split(';')
			ids = info[0].split('=')
			out = ''
			if ids[1] in dic:
				info[0] = ids[0] + '=' + dic[ids[1]]
				tmp[8] = ';'.join(info)
			out = '\t'.join(tmp)
			print(out)

if __name__ == '__main__':
	main()

