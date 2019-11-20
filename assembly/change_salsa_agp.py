#!/usr/bin/env python3 

def store_agp(agpFile):
	import re
	from collections import defaultdict
	dic = defaultdict(lambda: defaultdict(list))
	agpDic = defaultdict(list)

	patten = re.compile(r'(\S+)_([12])$')

	with open(agpFile) as f:
		for line in f:
			if line[0] == '#': continue
			line = line.rstrip()
			tmp = line.split('\t')
			if tmp[4] == 'N': continue
			scaf1 = tmp[5]
			match = patten.match(scaf1)
			idx = 1
			if match:
				scaf = match.group(1)
				idx = match.group(2)
			else:
				scaf = scaf1
			bg = int(tmp[6])
			ed = int(tmp[7])
			l = ed-bg+1
			dic[scaf][idx] = [scaf1, l]

	for scaf in dic:
		l1 = 0
		for idx in sorted(dic[scaf]):
			scaf1, l = dic[scaf][idx]
			agpDic[scaf1] = [scaf, l1]
			l1 += l

	return agpDic

def deal_agp(agpFile, agpDic):
	import re
	patten = re.compile(r'(\S+?)_([12])$')

	with open(agpFile) as f:
		for line in f:
			line = line.rstrip()
			if line[0] == '#':
				print(line)
				continue
			tmp = line.split('\t')
			if tmp[4] == 'N':
				print(line)
			else:
				scaf1 = tmp[5]
				match = patten.match(scaf1)
				idx = 1
				if match:
					scaf = match.group(1)
					idx = match.group(2)
				else:
					scaf = scaf1
				bg = int(tmp[6])
				ed = int(tmp[7])
				scaf, l1 = agpDic[scaf1]
				bg += l1
				ed += l1
				tmp[6] = str(bg)
				tmp[7] = str(ed)
				tmp[5] = scaf
				out = '\t'.join(tmp)
				print(out)

def main():
	import sys
	if len(sys.argv) != 2:
		sys.exit('python3 %s <in.agp>' % (sys.argv[0]))

	inFile = sys.argv[1]

	agpDic = store_agp(inFile)
	deal_agp(inFile, agpDic)

if __name__ == '__main__':
	main()

