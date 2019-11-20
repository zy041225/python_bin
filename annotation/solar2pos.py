#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
	sys.exit('python3 %s <solar>' % (sys.argv[0]))

inFile = sys.argv[1]

with open(inFile) as f:
	for line in f:
		line = line.rstrip()
		
