#!/usr/bin/env python3
import sys

def store(mapFile):
	from collections import defaultdict
	dic = defaultdict(list)
	with open(mapFile) as f:
		for line in f:
			line = line.rstrip()
			tmp = line.split('\t')
			koid = tmp[0]
			descript = tmp[1]
			dic[koid] = descript
	return dic

def main():
	if len(sys.argv) != 3:
		sys.exit('python3 %s <map_title.tab> <ko_map.tab>' % (sys.argv[0]))
	
	mapFile = sys.argv[1]
	ko_mapFile = sys.argv[2]

	dic = store(mapFile)

	with open(ko_mapFile) as f:
		for line in f:
			line = line.rstrip()
			tmp = line.split('\t')
			kid = tmp[0]
			for i in tmp[1].split():
				print('%s\tko%s\t%s' % (kid, i, dic[i]))

if __name__ == '__main__':
	main()

