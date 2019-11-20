#!/usr/bin/python3

def main():
	import sys
	import csv
	if len(sys.argv) != 3:
		sys.exit('python3 %s <hcluster> <species-lst>' % (sys.argv[0]))

	hcFile = sys.argv[1]
	lst = sys.argv[2].split('-')
	f = open(hcFile)
	for row in csv.reader(f, delimiter = '\t'):
		row[6] = row[6].rstrip(',')
		tmp = row[6].split(',')
		dic = {}
		for i in tmp:
			temp = i.split('_')
			if temp[-1] not in dic: dic[temp[-1]] = 0
			dic[temp[-1]] += 1
		flag = 0
		for spe in lst:
			if spe not in dic or dic[spe] != 1:
				flag = 1
				break
		if flag == 0:
			out = '\t'.join(row)
			print(out)

if __name__ == '__main__':
	main()

