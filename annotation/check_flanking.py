#!/usr/bin/env python3



def main():
	import sys
	if len(sys.argv) != 3:
		sys.exit('python3 %s <ort> <geneID> <flanking_number>' % (sys.argv[0]))

	ortFile = sys.argv[1]
	geneID = sys.argv[2]
	n = int(sys.argv[3])


