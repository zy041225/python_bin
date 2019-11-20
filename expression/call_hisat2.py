#!/usr/bin/python3

def get_fastq(info, indir):
	import os

	indir = os.path.abspath(indir)
	dic = {}

	f = open(info)
	for line in f:
		line = line.rstrip()
		srrID, species, tissue, sex = line.split('\t')[0:4]
		id = tissue + '_' + sex
		inpath = os.path.join(indir, id)
		for file in os.listdir(inpath):
			if file.startswith(srrID):
				if file.endswith('fq.gz') or file.endswith('fastq.gz') or file.endswith('fq') or file.endswith('fastq'):
					if id not in dic: dic[id] = {}
					fqFile = os.path.join(inpath, file)
					if '_1.' in file:
						if '-1' not in dic[id]: dic[id]['-1'] = []
						dic[id]['-1'].append(fqFile)
					if '_2.' in file:
						if '-2' not in dic[id]: dic[id]['-2'] = []
						dic[id]['-2'].append(fqFile)
					else:
						if '-U' not in dic[id]: dic[id]['-U'] = []
						dic[id]['-U'].append(fqFile)
	return dic

def call_hisat2(ref, fqDic, outdir):
	import os

	ref = os.path.abspath(ref)
	outdir = os.path.abspath(outdir)
	#hisat2 = '/hwfssz1/ST_DIVERSITY/PUB/USER/zhouyang/software/hisat2-2.0.4/hisat2'
	hisat2 = '/hwfssz1/ST_DIVERSITY/PUB/USER/zhouyang/software/hisat2-2.0.5/hisat2'
	samtools = '/share/app/samtools-1.2/bin/samtools'

	if not os.path.isdir(outdir): os.mkdir(outdir)
	
	fo = open(outdir + '/hisat2.sh', 'w')
	
	for id in sorted(fqDic):
		outpath = os.path.join(outdir, id)
		outfile = outpath + '/' + id + '.bam'
		if not os.path.isdir(outpath): os.mkdir(outpath)
		cmd = '%s -x %s ' % (hisat2, ref)
		for key in sorted(fqDic[id]):
			fqLst = ','.join(fqDic[id][key])
			cmd += '%s %s ' % (key, fqLst)
		cmd += '-q --phred33 -p 10 | %s view -b -@ 10 - -o %s' % (samtools, outfile)
		fo.write('%s\n' % (cmd))

def main():
	import sys

	if len(sys.argv) != 5:
		sys.exit('python3 %s <ref.index.prefix> <reads_info> <fqDir> <outDir>' % (sys.argv[0]))

	ref = sys.argv[1]
	info = sys.argv[2]
	indir = sys.argv[3]
	outdir = sys.argv[4]

	fqDic = get_fastq(info, indir)
	call_hisat2(ref, fqDic, outdir)

if __name__ == '__main__':
	main()

