#!/usr/bin/python3

def read_config(file):
	f = open(file)
	dic = {}
	for line in f:
		line = line.rstrip()
		tmp = line.split('\t')
		tissue, sample = tmp[0:2]
		dic[sample] = tissue
	return dic

def get_index(h, indic):
	from collections import defaultdict
	outdic = defaultdict(list)
	for sample in indic:
		idx = h.index(sample)
		outdic[indic[sample]].append(idx)
	return outdic

def main():
	import sys
	if len(sys.argv) != 3:
		sys.exit('python3 %s <lib.toNorm.rpkm> <mean.config>' % (sys.argv[0]))
	
	tabFile = sys.argv[1]
	confFile = sys.argv[2]

	dic = read_config(confFile)

	import csv
	f = open(tabFile)
	reader = csv.reader(f, delimiter = '\t')
	h = next(reader, None)
	index_dic = get_index(h, dic)
	oh = 'Sample'
	for tissue in sorted(index_dic):
		oh += '\t%s' % (tissue)
	print(oh)
	#sys.exit(h)
	import statistics
	for row in reader:
		out = row[0]
		out1 = row[0]
		for tissue in sorted(index_dic):
			#tmp = statistics.mean([ float(row[i]) for i in index_dic[tissue] ])
			#sys.exit(tmp)
			out += '\t%f' % (statistics.median([ float(row[i]) for i in index_dic[tissue] ]))
			out1 += '\t%f' % (statistics.stdev([ float(row[i]) for i in index_dic[tissue] ]))
		print(out)
		sys.stderr.write('%s\n' % out1)

if __name__ == '__main__':
	main()

