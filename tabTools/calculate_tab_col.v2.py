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

	return para_lst

def calculate(c, calculator):
	import statistics
	import sys
	
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
	from collections import defaultdict

	parser = argparse.ArgumentParser()
	parser.add_argument("tab", type=str, help="inputFile")
	parser.add_argument("group_lst", type=str, help="target column(s)")
	parser.add_argument("score_lst", type=str, help="score column")
	parser.add_argument("calculator", type=str, help="method")
	parser.add_argument("--header", help="file include header", action="store_true")
	args = parser.parse_args()

	col_lst = parameter_parser(args.group_lst)
	score_lst = parameter_parser(args.score_lst)

	f = open(args.tab)
	count = 0
	dic = defaultdict(lambda: defaultdict(list))

	for line in f:
		count += 1
		if args.header and count == 1:
			print(args.calculator)
			continue
		line = line.rstrip()
		tmp = line.split('\t')
		c = [tmp[i] for i in col_lst]
		id = '\t'.join(c)
		for i in score_lst:
			dic[id][i].append(float(tmp[i]))

	for id in sorted(dic):
		out = []
		out.append(id)
		for i in score_lst:
			score, c = calculate(dic[id][i], args.calculator)
			out.append(score)
		line = '\t'.join(str(i) for i in out)
		print(line)

if __name__ == '__main__':
	main()

