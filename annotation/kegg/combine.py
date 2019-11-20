#!/usr/bin/env python3
import sys

def store(tabFile):
	from collections import defaultdict
	dic = defaultdict(list)
	with open(tabFile) as f:
		for line in f:
			line = line.rstrip()
			tmp = line.split('\t')
			kid = tmp[0]
			koid = tmp[1]
			des = tmp[2]
			dic[kid].append([koid, des])
	return dic

def main():
	if len(sys.argv) != 3:
		sys.exit('python3 %s <ko_map.tab.format> <mart_export.txt.add.add_K.filt.lst>' % (sys.argv[0]))

	tabFile = sys.argv[1]
	lstFile = sys.argv[2]

	dic = store(tabFile)
	
	with open(lstFile) as f:
		for line in f:
			line = line.rstrip()
			tmp = line.split('\t')
			kid = tmp[0]
			if kid in dic:
				for koid, des in dic[kid]:
					print('%s\t%s\t%s' % (line, koid, des))
			else:
				print('%s\t-\t-' % (line))

if __name__ == '__main__':
	main()

