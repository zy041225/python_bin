#!/usr/bin/env python3

def read_pos(posFile):
	f = open(posFile)
	posDict = {}

	for line in f:
		line = line.rstrip()
		id, scaf, strand, bg, ed = line.split('\t')[:]
		bg = int(bg)
		ed = int(ed)
		if scaf not in posDict: posDict[scaf] = []
		posDict[scaf].append([id, strand, bg, ed])

	return posDict

def ovlLen(bg1, ed1, bg2, ed2):
	ovl = 0
	if bg1 <= bg2 and ed1 >= bg2:
		if ed1 > ed2:
			ovl = ed2-bg2+1
		else:
			ovl = ed1-bg2+1
	elif bg1 > bg2 and bg1 <= ed2:
		if ed1 >= ed2:
			ovl = ed2-bg1+1
		else:
			ovl = ed1-bg1+1
	return ovl

def findOverlap(posFile, posDict, strandFlag):
	f = open(posFile)
	
	for line in f:
		line = line.rstrip()
		id, scaf, strand, bg, ed = line.split('\t')[:]
		bg = int(bg)
		ed = int(ed)
		l = ed-bg+1
		if scaf not in posDict:
			print('%s\t%i\t0' % (line, l))
		else:
			dic = {}
			for info in posDict[scaf]:
				id1, strand1, bg1, ed1 = info[:]
				l1 = ed1-bg1+1
				if strandFlag == 1:	
					if strand == strand1:
						ovl = ovlLen(bg, ed, bg1, ed1)
				else:
					ovl = ovlLen(bg, ed, bg1, ed1)
				if ovl:
					dic[id1] = [strand1, l1, ovl]
			n = len(dic)
			if n > 0:
				s = ''
				for id1 in sorted(dic):
					strand1, l1, ovl1 = dic[id1][:]
					s += '%s,%s,%i,%i\t' % (id1, strand1, l1, ovl1)
				s = s.rstrip('\t')
				print('%s\t%i\t%i\t%s' % (line, l, n, s))
			else:
				print('%s\t%i\t%i' % (line, l, n))
				
def main():
	import sys

	if len(sys.argv) != 4:
		sys.exit('python3 %s <a.pos> <b.pos> <stranded[0|1]>' % (sys.argv[0]))

	aposFile = sys.argv[1]
	bposFile = sys.argv[2]
	strandFlag = int(sys.argv[3])

	posDict = read_pos(aposFile)
	findOverlap(bposFile, posDict, strandFlag)

if __name__ == '__main__':
	main()

