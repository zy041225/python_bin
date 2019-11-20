#!/usr/bin/python3

def call_fastq_dump(file, indir, outdir):
	import os
	import sys

	outdir = os.path.abspath(outdir)
	indir = os.path.abspath(indir)

	fd = '/hwfssz1/ST_DIVERSITY/PUB/USER/zhouyang/software/sratoolkit-2.8.2-1/bin/fastq-dump'

	if not os.path.isdir(outdir): os.mkdir(outdir)
	
	f = open(file)
	for line in f:
		line = line.rstrip()
		srrID, species, tissue, sex = line.split('\t')[0:4]
		path = os.path.join(outdir, tissue+'_'+sex)
		if not os.path.isdir(path): os.mkdir(path)
		srrFile = os.path.join(indir, srrID)
		srrFile += '/' + srrID + '.sra'
		if not os.path.exists(srrFile):
			sys.stderr.write('%s not found!\n' % (srrFile))
		else:
			print('%s --gzip --split-3 --outdir %s %s' % (fd, path, srrFile))

def main():
	import sys
	if len(sys.argv) != 4:
		sys.exit('python3 %s <read_info> <srr_dir> <outdir>' % (sys.argv[0]))

	info = sys.argv[1]
	indir = sys.argv[2]
	outdir = sys.argv[3]

	call_fastq_dump(info, indir, outdir)

if __name__ == '__main__':
	main()

