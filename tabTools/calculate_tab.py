#!/usr/bin/python3

def parameter_parser(argv):
	para_lst = []
	tmp = argv.split(',')
	for i in tmp:
		if '-' in i:
			bg, ed = i.split('-')[:]
			bg = int(bg)-1
			ed = int(ed)
			for j in range(bg, ed):
				para_lst.append(j)
		else:
			i = int(i)-1
			para_lst.append(int(i))

	return sorted(para_lst)

def calculate(lst, col_lst, calculator):
	import statistics
	import sys

	c = [float(lst[i]) for i in col_lst]

	if calculator == 'sum':
		return sum(c), c
	elif calculator == 'max':
		return max(c), c
	elif calculator == 'min':
		return min(c), c
	elif calculator == 'mean':
		return statistics.mean(c), c
	elif calculator == 'median':
		return statistics.median(c), c
	else:
		sys.exit('not defined function in the script\n')

def main():
	import sys
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument("tab", type=str, help="inputFile")
	parser.add_argument("column_lst", type=str, help="target column(s)")
	parser.add_argument("calculator", type=str, help="method")
	parser.add_argument("--header", help="file include header", action="store_true")
	args = parser.parse_args()

	#if len(sys.argv) != 4:
	#	sys.exit('python3 %s <tab> <column_lst> <calculator> --header' % (sys.argv[0]))

	#tab = sys.argv[1]
	#para = sys.argv[2]
	#calculator = sys.argv[3]
	col_lst = parameter_parser(args.column_lst)

	f = open(args.tab)
	count = 0
	for line in f:
		count += 1
		if args.header and count == 1:
			print(args.calculator)
			continue
		line = line.rstrip()
		tmp = line.split('\t')
		score, c = calculate(tmp, col_lst, args.calculator)
		print(score)

if __name__ == '__main__':
	main()

