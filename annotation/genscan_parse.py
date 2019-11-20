#!/usr/bin/env python3

import sys
import os
import re
from collections import defaultdict

def main():
	if len(sys.argv) != 3:
		sys.exit('python3 %s <genscan.out> <outdir>' % (sys.argv[0]))

	inFile = sys.argv[1]
	outDir = sys.argv[2]
	outDir = os.path.abspath(outDir)

	scaf = ''
	dic = defaultdict(list)

	basename = os.path.basename(inFile)

	gffFile = os.path.join(outDir, '%s.gff' % (basename))
	cdsFile = os.path.join(outDir, '%s.cds' % (basename))
	pepFile = os.path.join(outDir, '%s.pep' % (basename))

	cdsOut = open(cdsFile, 'w')
	pepOut = open(pepFile, 'w')

	pepPattern = re.compile(r'GENSCAN_predicted_peptide_(\d+)\|')
	cdsPattern = re.compile(r'GENSCAN_predicted_CDS_(\d+)\|')

	with open(inFile) as f:
		for line in f:
			line = line.rstrip()
			if line.startswith('Sequence '):
				scaf = line.split()[1]
			if line.startswith('Gn.Ex '):
				line = f.readline()
				line = f.readline()
				while(1):
					line = f.readline()
					line = line.rstrip()
					if line == '': continue
					if 'Predicted peptide sequence(s):' in line: break
					tmp = line.split()
					if tmp[1] == 'PlyA' or tmp[1] == 'Prom': continue
					id = tmp[0]
					id = id.split('.')[0]
					strand = tmp[2]
					start = int(tmp[3])
					end = int(tmp[4])
					frame = int(tmp[6])
					score = float(tmp[12])
					if start > end:
						start, end = end, start
					dic[id].append([scaf, strand, start, end, frame, score])
			if line == '': continue
			if line[0] == '>':
				if 'GENSCAN_predicted_peptide_' in line:
					match = pepPattern.findall(line)
					id = match[0]
					pepOut.write('>%s\n' % (id))
					while(1):
						line = f.readline()
						line = line.rstrip()
						if line == '': break
						pepOut.write('%s\n' % (line))
				if 'GENSCAN_predicted_CDS_' in line:
					match = cdsPattern.findall(line)
					id = match[0]
					cdsOut.write('>%s\n' % (id))
					while(1):
						line = f.readline()
						line = line.rstrip()
						if line == '': break
						cdsOut.write('%s\n' % (line))
			
	with open(gffFile, 'w') as fout:
		for id in sorted(dic.keys()):
			dic[id].sort(key=lambda x: x[3])
			bg = dic[id][0][2]
			ed = dic[id][-1][3]
			scaf = dic[id][0][0]
			strand = dic[id][0][1]
			fout.write('%s\tGenscan\tmRNA\t%i\t%i\t.\t%s\t.\tID=%s;\n' % (scaf, bg, ed, strand, id))
			for i in dic[id]:
				scaf, strand, start, end, frame, score = i[:]
				fout.write('%s\tGenscan\tCDS\t%i\t%i\t%f\t%s\t%i\tParent=%s;\n' % (scaf, start, end, score, strand, frame, id))

if __name__ == '__main__':
	main()

