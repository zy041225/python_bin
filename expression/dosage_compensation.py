#!/usr/bin/evn python3 

import sys

def main():
	if len(sys.argv) != 2:
		sys.exit('python3 %s <echidna.lib.toNorm.rpkm.cut.median>' % (sys.argv[0]))

	tabFile = sys.argv[1]

	import csv
	f = open(tabFile)
	reader = csv.reader(f, delimiter = '\t')
	h = next(reader, None)
	hout = '\t'.join(h)
	for i in range(1, len(h), 2):
		tis = h[i].split('_')[0]
		hout += '\t%s' % (tis)
	print(hout)

	for row in reader:
		out = '\t'.join(row)
		for i in range(1,len(row),2):
			if float(row[i]) >= 1.0 and float(row[i+1]) >= 1.0:
				ratio = float(row[i])/float(row[i+1])
				out += '\t%.6f' % (ratio)
			else:
				out += '\tNA'

		print(out)

if __name__ == '__main__':
	main()

