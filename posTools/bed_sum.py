#!/usr/bin/python3

def merge_bed(bedFile):
	f = open(bedFile)
	dic = {}
	for line in f:
		line = line.rstrip()
		tmp = line.split('\t')
		chr = tmp[0]
		bg = int(tmp[1])
		ed = int(tmp[2])
		id = tmp[3]
		if id not in dic: dic[id] = 0
		dic[id] += ed-bg
	for i in dic:
		print('%s\t%i' % (i, dic[i]))

def main():
	import sys
	if len(sys.argv) != 2:
		sys.exit('python3 %s <bed>' % (sys.argv[0]))

	bedFile = sys.argv[1]
	merge_bed(bedFile)

if __name__ == '__main__':
	main()

