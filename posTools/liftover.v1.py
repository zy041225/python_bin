#!/usr/bin/python3

def store_agp(agpFile):
	from collections import defaultdict
	agpDic = defaultdict(list)

	with open(agpFile) as f:
		for line in f:
			line = line.rstrip()
			tmp = line.split('\t')
			if tmp[4] == 'N': continue
			chr = tmp[0]
			start = int(tmp[1])
			end = int(tmp[2])
			idx = int(tmp[3])
			scaf = tmp[5]
			bg = int(tmp[6])
			ed = int(tmp[7])
			orient = tmp[8]
			agpDic[scaf].append([bg, ed, chr, start, end, orient])
	return agpDic

def process(agpDic, bedFile):
	with open(bedFile) as f:
		for line in f:
			line = line.rstrip()
			tmp = line.split('\t')
			scaf = tmp[0]
			bg = int(tmp[1])
			ed = int(tmp[2])
			id = tmp[3]
			score = tmp[4]
			strand = tmp[5]
			bg += 1
			[chr, bg2, ed2, strand2] = lift_bed(agpDic, scaf, bg, ed, strand)
			if chr == '': continue
			bg2 -= 1
			print('%s\t%i\t%i\t%s\t%s\t%s' % (chr, bg2, ed2, id, score, strand2))

def lift_bed(agpDic, scaf, bg1, ed1, strand):
	import sys
	from find_overlap import ovlLen

	bg2 = 0
	ed2 = 0
	strand2 = ''

	if scaf in agpDic:
		for i in agpDic[scaf]:
			bg, ed, chr, start, end, orient = i[:]
			ovl = ovlLen(bg, ed, bg1, ed1)
			if ovl > 0:
				if ed1-bg1+1 > ovl:
					sys.stderr.write('element cross boundary:\n element: %s\t%i\t%i\n AGP block: %s\t%i\t%i\n' % (scaf, bg1, ed1, scaf, bg, ed))
					return ('', '', '', '')
				elif ed1-bg1+1 == ovl:
					if orient == '+':
						bg2 = bg1-bg+start
						ed2 = ed1-bg1+bg2
						strand2 = strand
					else:
						bg2 = ed-ed1+start
						ed2 = ed1-bg1+bg2
						strand2 = '+' if strand == '-' else '-'
					return (chr, bg2, ed2, strand2)
		sys.stderr.write('element not in AGP, please check:\n element: %s\t%i\t%i\n' % (scaf, bg1, ed1))
		return ('', '', '', '')

	else:
		sys.stderr.write('element not in AGP, please check:\n element: %s\t%i\t%i\n' % (scaf, bg1, ed1))
		return ('', '', '', '')

def main():
	import sys
	if len(sys.argv) != 3:
		sys.exit('python3 %s <agp> <bed>' % (sys.argv[0]))

	agpFile = sys.argv[1]
	bedFile = sys.argv[2]
	
	agpDic = store_agp(agpFile)
	process(agpDic,  bedFile)


if __name__ == '__main__':
	main()

