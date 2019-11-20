#!/usr/bin/python3

def main():
	import sys
	import os
	from index import read_info
	
	if len(sys.argv) != 6:
		sys.exit('python3 %s <reads.info> <gff> <hisat2.dir> <outdir> <fa>' % (sys.argv[0]))

	info = os.path.abspath(sys.argv[1])
	gffFile = os.path.abspath(sys.argv[2])
	indir = os.path.abspath(sys.argv[3])
	outdir = os.path.abspath(sys.argv[4])
	faFile = os.path.abspath(sys.argv[5])

	infoDic = read_info(info)
	cufflinks = '/share/app/cufflinks-2.2.1/cufflinks'

	for id in sorted(infoDic):
		l = infoDic[id][2]
		bamFile = os.path.join(indir, id, id+'.sort.bam')
		if not os.path.isfile(bamFile):
			sys.stderr.write('%s not found\n' % (bamFile))
		
		else:
			outdir1 = os.path.join(outdir, id)
			if not os.path.exists(outdir1): os.mkdir(outdir1)
			outprefix = os.path.join(outdir, id, id)
			print('{0} -p 10 -G {2} -b {3} -u {1} -o {4}'.format(cufflinks, bamFile, gffFile, faFile, outdir1))

if __name__ == '__main__':
	main()

