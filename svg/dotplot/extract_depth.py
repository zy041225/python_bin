#!/usr/bin/env python3

def store_nor(norFile):
	from collections import defaultdict
	import sys

	dic = defaultdict(dict)

	with open(norFile) as f:
		for line in f:
			line = line.rstrip()
			tmp = line.split('\t')
			if line[0] == '#': continue
			scafID, idx = tmp[0].split('#')[:]
			#if tmp[9] == 'NA':
			#	continue
			norM = float(tmp[7])
			norF = float(tmp[8])
			idx = int(idx)
			#ratio = float(tmp[9])
			dic[scafID][idx] = [norM, norF]
	return dic

def main():
	import sys
	import statistics

	if len(sys.argv) != 3:
		sys.exit('python3 %s <miss.out.tab> <mean.FM.win.2k.info.nor>' % (sys.argv[0]))

	tabFile = sys.argv[1]
	norFile = sys.argv[2]

	dic = store_nor(norFile)

	with open(tabFile) as f:
		for line in f:
			line = line.rstrip()
			tmp = line.split('\t')
			scafID = tmp[0]
			bg = int(tmp[2])
			ed = int(tmp[3])
			#dic[scaf].append([bg, ed])
			idxbg = int(bg/2000)
			idxed = int(ed/2000)
			scafID1 = tmp[5]
			bg1 = int(tmp[7])
			ed1 = int(tmp[8])
			idxbg1 = int(bg1/2000)
			idxed1 = int(ed1/2000)
			norm, norf, norm1, norf1 = [], [], [], []
			out, out1 = [], []
			if scafID in dic:
				for i in range(idxbg, idxed+1):
					if i not in dic[scafID]:
						continue
					norM = dic[scafID][i][0]
					norF = dic[scafID][i][1]
					#ratio = dic[scafID][i][2]
					norm.append(norM)
					norf.append(norF)
					out.append('%i\t%f\t%f' % (i, norM, norF))
					#print('%i\t%f\t%f\t%f' % (i, norM, norF, ratio))
			if scafID1 in dic:
				for i in range(idxbg1, idxed1+1):
					if i not in dic[scafID1]:
						continue
					norM = dic[scafID1][i][0]
					norF = dic[scafID1][i][1]
					#ratio = dic[scafID1][i][2]
					norm1.append(norM)
					norf1.append(norF)
					out1.append('%i\t%f\t%f' % (i, norM, norF))
					#print('%i\t%f\t%f\t%f' % (i, norM, norF, ratio))
			if norm == [] or norm1 == []:
				#sys.exit(line)
				continue
			norM = statistics.median(norm)
			norM1 = statistics.median(norm1)
			norF = statistics.median(norf)
			norF1 = statistics.median(norf1)
			print('%s\t%f\t%f\t%f\t%f' % (line, norM, norF, norM1, norF1))

if __name__ == '__main__':
	main()

