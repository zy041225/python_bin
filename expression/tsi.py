#!/usr/bin/python3

def main():
	import sys
	if len(sys.argv) != 2:
		sys.exit('python3 %s <rpkm.tab>' % (sys.argv[0]))

	tabFile = sys.argv[1]

	import csv
	f = open(tabFile)
	reader = csv.reader(f, delimiter = '\t')
	h = next(reader, None)
	hout = '\t'.join(h + ['TSI', 'TISSUE', 'max_exp', 'foldchange'])
	print(hout)

	import statistics
	for row in reader:
		dic = {}
		for i in range(1, len(row)):
			s = sum([float(row[j]) for j in range(1, len(row))])
			if s == 0:
				ratio = 0.0
			else:
				ratio = float(row[i])/s
			dic[h[i]] = ratio
		tissue = ''
		tsi = ''
		max_expr = '%.6f' % (max([float(i) for i in row[1:]]))
		order = sorted(dic, key=lambda x: dic[x], reverse=True)
		for i in range(len(order)):
			if dic[order[i]] == 0.0:
				tissue = 'NA'
				tsi = '0.0'
			else:
				tissue = order[i]
				tsi = '%.6f' % (dic[tissue])
			if dic[order[i+1]] == 0:
				foldchange = 'NA'
			else:
				foldchange = '%.6f' % (dic[order[i]]/dic[order[i+1]])
			break
		out = '\t'.join(row + [tsi, tissue, max_expr, foldchange])
		print(out)

if __name__ == '__main__':
	main()

