#!/usr/bin/env python3

def store_file(file, col_lst, sep):
	dic = {}
	with open(file) as f:
		for line in f:
			line = line.rstrip()
			tmp = line.split(sep)
			c = [tmp[i] for i in col_lst]
			id = sep.join(c)
			dic[id] = 1
	return dic

def filter_file(file, col_lst, dic, sep, t):
	with open(file) as f:
		for line in f:
			line = line.rstrip()
			tmp = line.split(sep)
			c = [tmp[i] for i in col_lst]
			id = sep.join(c)
			if t == 'same':
				if id in dic: print(line)
			elif t == 'diff':
				if id not in dic: print(line)

def main():
	import sys
	from calculate_tab_col import parameter_parser
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument("inputFile1", type=str, help="inputFile1")
	parser.add_argument("inputFile2", type=str, help="inputFile2")
	parser.add_argument("group_lst1", type=str, help="target column(s) in inputFile1")
	parser.add_argument("group_lst2", type=str, help="target column(s) in inputFile2")
	parser.add_argument("--t", type=str, dest='t', help="same or diff", default='same')
	parser.add_argument("--s1", type=str, dest='s1', help="separator in inputFile1", default='\t')
	parser.add_argument("--s2", type=str, dest='s2', help="separator in inputFile2", default='\t')
	args = parser.parse_args()

	col_lst1 = parameter_parser(args.group_lst1)
	col_lst2 = parameter_parser(args.group_lst2)

	dic = store_file(args.inputFile1, col_lst1, args.s1)
	filter_file(args.inputFile2, col_lst2, dic, args.s2, args.t)

if __name__ == '__main__':
	main()

