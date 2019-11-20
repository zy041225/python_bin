#!/usr/bin/python3

def main():
	import sys
	import os
	from index import read_info
	
	if len(sys.argv) != 5:
		sys.exit('python3 %s <reads.info> <gff> <hisat2.dir> <outdir>' % (sys.argv[0]))

	info = sys.argv[1]
	gffFile = os.path.abspath(sys.argv[2])
	indir = os.path.abspath(sys.argv[3])
	outdir = os.path.abspath(sys.argv[4])

	infoDic = read_info(info)
	stringtie = '/hwfssz1/ST_DIVERSITY/PUB/USER/zhouyang/software/stringtie-1.3.3b/stringtie'
	preDE = '/hwfssz1/ST_DIVERSITY/PUB/USER/zhouyang/software/stringtie-1.3.3b/prepDE.py'

	for id in sorted(infoDic):
		l = infoDic[id][2]
		bamFile = os.path.join(indir, id, id+'.sort.bam')
		if not os.path.isfile(bamFile):
			sys.stderr.write('%s not found\n' % (bamFile))
		
		else:
			outdir1 = os.path.join(outdir, id)
			if not os.path.exists(outdir1): os.mkdir(outdir1)
			outprefix = os.path.join(outdir, id, id)
			#print('{0} {1} -G {2} -p 10 -C {3}.coverage -A {3}.gene_abund.out -e > {3}.gtf; sed \'s/gene_id "STRG\.[0-9]\+";//\' {3}.gtf > {3}.mod.gtf; echo -e {6}\'\\t\'{3}.mod.gtf > {3}.lst; python {4} -i {3}.lst -l {5} -g {3}.gene_count_matrix.csv -t {3}.transcript_count_matrix.csv'.format(stringtie, bamFile, gffFile, outprefix, preDE, l, id))
			print('{0} {1} -G {2} -p 10 -C {3}.coverage -A {3}.gene_abund.out -e > {3}.gtf; perl -lane \'$_=~s/gene_id ".+?"; //; print $_\' {3}.gtf > {3}.mod.gtf; echo -e {6}\'\\t\'{3}.mod.gtf > {3}.lst; /hwfssz1/ST_DIVERSITY/PUB/USER/zhouyang/software/python-2.7.13/bin/python {4} -i {3}.lst -l {5} -g {3}.gene_count_matrix.csv -t {3}.transcript_count_matrix.csv'.format(stringtie, bamFile, gffFile, outprefix, preDE, l, id))
if __name__ == '__main__':
	main()

