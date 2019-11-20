#!/usr/bin/env python3
import re
import sys

def store_ko(koFile):
	dic = {}
	pattern = re.compile(r'^(\d+).+')
	
	with open(koFile) as f:
		for line in f:
			line = line.rstrip()
			if line.startswith('ENTRY'):
				ko_id = line.split()[1]
			if 'HSA: ' in line:
				line1 = line.split('HSA: ')[1]
				tmp = line1.split()
				for i in tmp:
					match = pattern.match(i)
					if not match: sys.exit('%s\n%s' % (line, i))
					num = str(match.group(1))
					dic[num] = ko_id
	return dic


def main():
	if len(sys.argv) != 3:
		sys.exit('python3 %s <ko> <mart_export.txt.add>' % (sys.argv[0]))

	koFile = sys.argv[1]
	tabFile = sys.argv[2]

	dic = store_ko(koFile)	

	with open(tabFile) as f:
		for line in f:
			line = line.rstrip()
			num = line.split('\t')[1]
			if num in dic:
				print('%s\t%s' % (line, dic[num]))
			else:
				print('%s\tNA' % (line))


if __name__ == '__main__':
	main()

