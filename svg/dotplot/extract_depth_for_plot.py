#!/usr/bin/env python3

import sys
from extract_depth import store_nor
from math import floor

def main():
	if len(sys.argv) != 4:
		sys.exit('python3 %s <pos> <norm.info> <win_size>' % (sys.argv[0]))

	posFile = sys.argv[1]
	infoFile = sys.argv[2]
	size = int(sys.argv[3])

	dic = store_nor(infoFile)
	
	with open(posFile) as f:
		for line in f:
			line = line.rstrip()
			tmp = line.split('\t')
			id = tmp[0]
			scaf = tmp[1]
			strand = tmp[2]
			bg = int(tmp[3])
			ed = int(tmp[4])
			bg -= 1
			ed -= 1
			bgidx = floor(bg/size)
			edidx = floor(ed/size)
			for i in range(bgidx, edidx):
				start = i*size+1
				end = (i+1)*size
				norM, norF = dic[scaf][i][:]
				print('%s\t%i\t%i\t%.4f\tmale\tdep' % (scaf, start, end, norM))
				print('%s\t%i\t%i\t%.4f\tfemale\tdep' % (scaf, start, end, norF))

if __name__ == "__main__":
	main()

