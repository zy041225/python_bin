#!/usr/bin/python3

def get_gene_source(gffFile):
	import re

	pattern_shift = re.compile(r'Shift=(\d+);')
	dic = {}

	f = open(gffFile)
	for line in f:
		line = line.rstrip()
		tmp = line.split('\t')
		if tmp[2] == 'mRNA':
			temp = tmp[8].split(';')
			id = temp[0].split('=')[1]
			transcript = ''
			if id.startswith('ENS'):
				source = id.split('-D')[0]
			elif re.match(r'^A\d+$', id):
				source = 'denovo'
			elif re.match(r'MSTRG.(\d+)', id):
				source = 'transcript'

			match = pattern_shift.findall(tmp[8])
			shift = 0
			if match: shift = int(match[0])
			print('%s\t%s\t%i' % (id, source, shift))

def main():
	import sys
	if len(sys.argv) != 2:
		sys.exit('python3 %s <gff>' % (sys.argv[0]))
	get_gene_source(sys.argv[1])
	

if __name__ == '__main__':
	main()

