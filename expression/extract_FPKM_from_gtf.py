#!/usr/bin/python3

def main():
	import sys
	import re

	if len(sys.argv) != 2:
		sys.exit('python3 %s <gtf>' % (sys.argv[0]))

	gtfFile = sys.argv[1]
	pattern_tra = re.compile(r'transcript_id "(\S+?)";')
	pattern_fpkm = re.compile(r'FPKM "(\S+?)";')

	f = open(gtfFile)
	for line in f:
		if line[0] == '#': continue
		line = line.rstrip()
		tmp = line.split('\t')
		if tmp[2] != 'transcript': continue
		match_tra = pattern_tra.findall(tmp[8])
		match_fpkm = pattern_fpkm.findall(tmp[8])
		id = match_tra[0]
		fpkm = float(match_fpkm[0])
		print('%s\t%f' % (id, fpkm))

if __name__ == '__main__':
	main()

