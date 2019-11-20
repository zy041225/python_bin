#!/usr/bin/python3

def create_sh(dic, indir, outdir, gff):
	import sys
	import os
	script = '/hwfssz1/ST_DIVERSITY/PUB/USER/zhouyang/bin/BAMforGene/0.creat.sh.pl'

	indir = os.path.abspath(indir)
	outdir = os.path.abspath(outdir)
	gff = os.path.abspath(gff)

	for id in sorted(dic):
		inpath = os.path.join(indir, id)
		if os.path.isdir(inpath):
			for file in os.listdir(inpath):
				if file.endswith('.sort.bam'):
					bamFile = os.path.join(inpath, file)
					length = dic[id][2]

					outpath = os.path.join(outdir, id)
					if not os.path.isdir(outpath): os.mkdir(outpath)
					fo = open(outpath + '/work.sh', 'w')
					fo.write('perl %s --BAM %s --Gff %s --ratio 0.5 --Split 5 --Res %s.rpkm --rL %i --Unique\n' % (script, bamFile, gff, id, length))
					fo.write('sed -i \'s/sh /qsub -cwd -l vf=0.2g,num_proc=1 -q st.q -P P18Z10200N0122 /g\' step1.get.num.sh\n')
					fo.close()
					os.chdir(outpath)
					os.system('sh work.sh')
					os.system('sh step1.get.num.sh')
					os.chdir(outdir)
		else:
			sys.stderr.write('%s not found\n' % (path))

def main():
	import sys
	from index import read_info

	if len(sys.argv) != 5:
		sys.exit('python3 %s <read_info> <gff> <bam_dir> <outdir>' % (sys.argv[0]))

	info = sys.argv[1]
	gff = sys.argv[2]
	indir = sys.argv[3]
	outdir = sys.argv[4]

	infoDic = read_info(info)
	create_sh(infoDic, indir, outdir, gff)

if __name__ == '__main__':
	main()

