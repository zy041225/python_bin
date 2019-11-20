#!/usr/bin/python3

def read_bed(bedFile):
	f = open(bedFile)
	dic = {}

	for line in f:
		line = line.rstrip()
		tmp = line.split('\t')[:]
		scaf = tmp[0]
		bg = int(tmp[1])
		ed = int(tmp[2])
		if scaf not in dic: dic[scaf] = []
		dic[scaf].append([bg, ed])
	
	return dic

def mafExtract(maf, posDict, spe):
	from Bio import AlignIO
	import sys
	from maf2pos import maf2pos

	for msa in AlignIO.parse(maf, 'maf'):
		posInfo = maf2pos(msa)
		

def main():
	import sys

	if len(sys.argv) != 4:
		sys.exit('python3 %s <maf> <bed> <spe>' % (sys.argv[0]))
	
	mafFile = sys.argv[1]
	bedFile = sys.argv[2]
	spe = sys.argv[3]

	bedDict = read_bed(bedFile)
	mafExtract(mafFile, posDict, spe)

