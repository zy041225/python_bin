#!/usr/bin/python3

def process(agpDic, gffFile):
	from liftover import lift_bed
	import sys

	with open(gffFile) as f:
		for line in f:
			line = line.rstrip()
			if line[0] == '#':
				print(line)
				continue
			tmp = line.split('\t')
			scaf = tmp[0]
			bg = int(tmp[3])
			ed = int(tmp[4])
			strand = tmp[6]
			[chr, bg2, ed2, strand2] = lift_bed(agpDic, scaf, bg, ed, strand)
			if chr == 0 and bg2 == 0 and ed2 == 0 and strand2 == 0:
				sys.stderr.write('%s on %s is not in AGP, abandon\n' % (line, scaf))
			elif chr == 1 and bg2 == 1 and ed2 == 1 and strand2 == 1:
				sys.stderr.write('%s cross boundary, abandon\n' % (line))
			else:
				tmp[0] = chr
				tmp[3] = str(bg2)
				tmp[4] = str(ed2)
				tmp[6] = strand2
				out = '\t'.join(tmp)
				print(out)

def main():
	import sys
	from liftover import store_agp

	if len(sys.argv) != 3:
		sys.exit('python3 %s <agp> <gff>' % (sys.argv[0]))

	agpFile = sys.argv[1]
	gffFile = sys.argv[2]
	
	agpDic = store_agp(agpFile)
	process(agpDic,  gffFile)


if __name__ == '__main__':
	main()

