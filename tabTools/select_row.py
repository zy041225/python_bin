#!/usr/bin/env python3

def main():
	import sys
	from collections import defaultdict
	sys.path.append('/hwfssz1/ST_DIVERSITY/PUB/USER/zhouyang/python_bin/tabTools/')
	from calculate_tab_col import parameter_parser

	if len(sys.argv) != 5:
		sys.exit('python3 %s <tab> <col_lst> <occurence> <top|one>' % (sys.argv[0]))

	tabFile = sys.argv[1]
	colLst = parameter_parser(sys.argv[2])
	ocur = int(sys.argv[3])
	typ = sys.argv[4]

	dic = defaultdict(lambda: 0)

	with open(tabFile) as f:
		for line in f:
			line = line.rstrip()
			tmp = line.split('\t')
			flag = 0
			key = '\t'.join(tmp[i] for i in colLst)
			dic[key] += 1
			if typ == 'top':
				if ocur >= dic[key]: flag = 1
			if typ == 'one':
				if ocur == dic[key]: flag = 1
			if flag == 1: print(line)

if __name__ == '__main__':
	main()

