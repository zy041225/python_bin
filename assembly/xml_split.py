#!/usr/bin/env python3

import sys
import xml.etree.ElementTree as ET

def main():
	if len(sys.argv) != 3:
		sys.exit('python3 %s <arrow.xml> <outdir>' % (sys.argv[0]))

	inFile = sys.argv[1]
	outdir = sys.argv[2]

	tree = ET.parse(inFile)
	root = tree.getroot()
	
	for child in root.iter('pbds:Filters'):
		tree.write('')

if __name__ == '__main__':
	main()

