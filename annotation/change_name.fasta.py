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
		sys.exit('python3 %s <ID_name.lst> <fasta>' % (sys.argv[0]))
	
	lstFile = sys.argv[1]
	faFile = sys.argv[2]

	dic = store(lstFile)

	with open(faFile) as f:
		for line in f:
			line = line.rstrip()
			if line[0] == '>':
				id = line.split()[0]
				id = id[1:]
				if id in dic:
					print('>%s' % (dic[id]))
				else:
					print('>%s' % (id))
			else:
				print(line)

if __name__ == '__main__':
	main()

