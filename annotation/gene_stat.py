#!/usr/bin/python3

def store_gff(gffFile):
	import sys
	dic = {}

	f = open(gffFile)
	for line in f:
		line = line.rstrip()
		tmp = line.split('\t')
		tmp[2] = tmp[2].upper()
		if tmp[2].startswith('UTR') or tmp[2] == 'MRNA': continue
		if tmp[2] == 'CDS':
			info = tmp[8].split(';')[0]
			id = info.split('=')[1]
			bg = int(tmp[3])
			ed = int(tmp[4])
			if id not in dic: dic[id] = []
			dic[id].append([bg, ed])
		else:
			sys.exit(line+'\n')
	return dic

def get_mRNA_len(cds_lst):
	mRNA_len = 0
	for i in cds_lst:
		mRNA_len += i[1]-i[0]+1
	return mRNA_len

def get_gene_len(cds_lst):
	cds_lst = sorted(cds_lst, key=lambda x: x[0])
	gene_len = cds_lst[-1][1]-cds_lst[0][0]+1
	return gene_len

def get_intron_len(cds_lst):
	intron_len = 0
	cds_lst = sorted(cds_lst, key=lambda x: x[0])
	for i in range(len(cds_lst)-1):
		bg1, ed1 = cds_lst[i][:]
		bg2, ed2 = cds_lst[i+1][:]
		intron_bg = ed1+1
		intron_ed = bg2-1
		intron_len += intron_ed-intron_bg+1
	return intron_len

def main():
	import sys

	if len(sys.argv) != 2:
		sys.exit('python3 %s <gff>' % (sys.argv[0]))

	gffFile = sys.argv[1]
	dic = store_gff(gffFile)
	for i in sorted(dic):
		mRNA_len = get_mRNA_len(dic[i])
		gene_len = get_gene_len(dic[i])
		intron_len = get_intron_len(dic[i])
		exon_num = len(dic[i])
		if exon_num > 1:
			print('%s\t%i\t%i\t%i\t%.2f\t%.2f' % (i, gene_len, mRNA_len, exon_num, mRNA_len/exon_num, intron_len/(exon_num-1)))
		else:
			print('%s\t%i\t%i\t%i\t%.2f\t0.00' % (i, gene_len, mRNA_len, exon_num, mRNA_len/exon_num))

if __name__ == '__main__':
	main()

