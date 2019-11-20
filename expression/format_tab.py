#!/usr/bin/python3

def main():
	import sys
	if len(sys.argv) != 2:
		sys.exit('python3 %s <sample_name.tissue.sex.tab.add>' % (sys.argv[0]))

	tabFile = sys.argv[1]

	dic = {'br': 'brain', 'ts': 'testis', 'pl': 'placenta', 'ov': 'ovary', 'kd': 'kidney', 'lv': 'liver', 'cb': 'cerebellum', 'ht': 'heart'}

	f = open(tabFile)
	for line in f:
		line = line.rstrip()
		tmp = line.split('\t')
		gsmid = tmp[0]
		temp = tmp[1].split()
		spe = temp[0]
		tissue = dic[temp[1]]
		batch = ''
		sex = ''
		if temp[-1][0] == '[':
			batch = tmp[2] + '_' + temp[-1]
			sex = ''.join(temp[2:-1])
		else:
			batch = tmp[2]
			sex = ''.join(temp[2:])
		print('%s\t%s\t%s\t%s\t%s' % (gsmid, spe, tissue, sex, batch))

if __name__ == "__main__":
	main()

