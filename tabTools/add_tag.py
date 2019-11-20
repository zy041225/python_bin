#!/usr/bin/env python3

import sys
import getopt

if len(sys.argv) != 6 or sys.argv[5] == '-':
	sys.exit("python3 %s <tab> <tab_column> <tag_lst> <tag_column> <tag_name>\n<tag_name> should NOT be '-'"% (sys.argv[0]))

dict = {}
tag_lst = open(sys.argv[3])
for line in tag_lst:
	line = line.rstrip()
	tmp = line.split('\t')
	dict[tmp[int(sys.argv[4])-1]] = 1

tab = open(sys.argv[1])
for line in tab:
	line = line.rstrip()
	tmp = line.split('\t')
	tag = '-'
	if tmp[int(sys.argv[2])-1] in dict:
			tag = sys.argv[5]
	line += '\t%s' % (tag)
	print(line)
