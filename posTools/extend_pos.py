#!/usr/bin/env python3

def store(lenFile):
	dic = {}
	with open(lenFile) as f:
		for line in f:
			line = line.rstrip()
			tmp = line.split('\t')
			scaf = tmp[0]
			l = int(tmp[1])
			dic[scaf] = l
	return dic

def main():
	import sys
	if len(sys.argv) != 4:
		sys.exit('python3 %s <pos> <genome.len> <extend_length>' % (sys.argv[0]))

	inFile = sys.argv[1]
	lenFile = sys.argv[2]
	ext = int(sys.argv[3])

	dic = store(lenFile)

	with open(inFile) as f:
		for line in f:
			line = line.rstrip()
			tmp = line.split('\t')
			scaf = tmp[1]
			start = int(tmp[3])
			end = int(tmp[4])
			start = start - ext
			if start - ext < 1: start = 1
			end = end + ext
			if end > dic[scaf]: end = dic[scaf]
			print('%s\t%s\t%s\t%i\t%i' % (tmp[0], scaf, tmp[2], start, end))

if __name__ == '__main__':
	main()

