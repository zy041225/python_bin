#!/usr/bin/python3

def maf2pos(msa):
	posInfo = {}

	for seqrec in msa:
		#spe, scaf = seqrec.id.split('.', 1)[:]
		bg = int(seqrec.annotations['start'])
		l = int(seqrec.annotations['size'])
		strand = int(seqrec.annotations['strand'])
		size = int(seqrec.annotations['srcSize'])

		bg += 1
		ed = 0
		if strand == 1:
			strand = '+'
			ed = bg+l-1
		else:
			ed = size-bg+1
			bg = ed-l+1
			strand = '-'
		posInfo[seqrec.id] = [strand, bg, ed]

	return posInfo

def output(file):
	from Bio import AlignIO

	idx = 1
	for msa in AlignIO.parse(file, 'maf'):
		posInfo = maf2pos(msa)
		for id in sorted(posInfo.keys()):
			strand, bg, ed = posInfo[id]
			spe, scaf = id.split('.', 1)[:]
			print('%i-%s-%s\t%s\t%s\t%i\t%i' % (idx, spe, scaf, scaf, strand, bg, ed))
		idx += 1

def main():
	import sys

	if len(sys.argv) != 2:
		sys.exit('python3 %s <maf>' % (sys.argv[0]))

	file = sys.argv[1]
	output(file)

if __name__ == '__main__':
	main()

