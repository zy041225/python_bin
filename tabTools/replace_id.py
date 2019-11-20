#!/usr/bin/env python3

def main():
	import sys

	if len(sys.argv) != 4:
		sys.exit('python3 %s <relation.tab> <in.tab> <column>' % (sys.argv[0]))

	relTab = sys.argv[1]
	inFile = sys.argv[2]
	col = int(sys.argv[3])-1

	dic = {}

	with open(relTab) as f:
		for line in f:
			line = line.rstrip()
			tmp = line.split('\t')
			dic[tmp[0]] = tmp[1]

	with open(inFile) as f:
		for line in f:
			line = line.rstrip()
			tmp = line.split('\t')
			tmp[col] = dic[tmp[col]]
			out = '\t'.join(tmp)
			print(out)

if __name__ == '__main__':
	main()

