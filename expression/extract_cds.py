#!/usr/bin/python3

def main():
	import sys
	import csv
	import os

	if len(sys.argv) != 4:
		sys.exit('python3 %s <tmp1.add.add> <cds> <outdir>' % (sys.argv[0]))

	tabFile = sys.argv[0]
	cdsFile = sys.argv[1]
	outdir = os.path.abspath(sys.argv[2])

	fish = '/hwfssz1/ST_DIVERSITY/PUB/USER/zhouyang/bin/seq_related/fishInWinter.pl'

	f = open(tabFile)
	for row in csv.reader(f, delimiter = '\t'):
		row[-1] = row[-1].rstrip(',')
		tmp = row[-1].split(',')
		outpath = os.path.join(outdir, row[0])
		if not os.path.exists(outpath): os.mkdir(outpath)
		outLst = outpath + '/' + row[0] + '.lst'
		fo = open(outLst, 'w')
		out = '\n'.join(tmp)
		fo.write(out + '\n')
		fo.close()
		fo = open(outpath + '/' + row[0] + '.sh', 'w')
		fo.write('perl %s -bf table -ff fasta ')

if __name__ == '__main__':
	main()

