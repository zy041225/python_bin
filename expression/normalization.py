#!/usr/bin/python3

def store(file, col, h=False):
	dic = {}

	f = open(file)
	import csv
	reader = csv.reader(f, delimiter = '\t')
	if h: next(reader, None)
	for row in reader:
		dic[row[0]] = row[col-1]
	
	return dic

def main():
	import sys
	import csv
	import pandas as pd
	
	if len(sys.argv) != 4:
		sys.exit('python3 %s <norm.factors.txt> <gff.stat> <gene_count_matrix.tab>' % (sys.argv[0]))

	normFile = sys.argv[1]
	statFile = sys.argv[2]
	tabFile = sys.argv[3]

	normDic = store(normFile, 2, h=True)
	statDic = store(statFile, 3)
	
	df = pd.read_csv(tabFile, sep = '\t')
	#df_num = df.copy()
	df_rpkm = df.copy()

	avg = df.sum(axis=0).mean()

	for i in normDic:
		df_rpkm[i] = df[i]*1e3*1e6/int(float(normDic[i])*avg)

	for i in df_rpkm.index:
		df_rpkm.loc[i] = df_rpkm.loc[i]/float(statDic[i])
	
	df_rpkm.to_csv(sys.stdout, sep = '\t', quoting = csv.QUOTE_NONE)
	#print(df_rpkm.to_string())

if __name__ == '__main__':
	main()

