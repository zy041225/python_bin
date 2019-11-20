#!/usr/bin/python3

def read_info(info):
	f = open(info)
	dic = {}

	for line in f:
		line = line.rstrip()
		srrID, species, tissue, sex, length = line.split('\t')[0:5]
		id = '%s_%s' % (tissue, sex)
		dic[id] = [srrID, species, int(length)]

	return dic

def call_samtools(dic, indir):
	samtools = '/share/app/samtools-1.2/bin/samtools'
	import os
	import sys
	import re

	indir = os.path.abspath(indir)

	for id in sorted(dic):
		path = os.path.join(indir, id)
		if os.path.isdir(path):
			for file in os.listdir(path):
				if file.endswith('bam'):
					file = os.path.join(path, file)
					bam = re.sub(r'.bam$', '.sort', file)
					bamfile = bam + '.bam'
					print('%s sort %s %s; %s index %s' % (samtools, file, bam, samtools, bamfile))
		else:
			sys.stderr.write('%s not found\n' % (path))

def main():
	import sys

	if len(sys.argv) != 3:
		sys.exit('python3 %s <read_info> <bam_dir>' % (sys.argv[0]))

	info = sys.argv[1]
	indir = sys.argv[2]

	infoDic = read_info(info)
	call_samtools(infoDic, indir)

if __name__ == '__main__':
	main()

