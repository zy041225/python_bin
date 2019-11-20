#!/usr/bin/python3

def main():
	import sys
	if len(sys.argv) != 2:
		sys.exit('python3 %s <aln>' % (sys.argv[0]))

	alnFile = sys.argv[1]

	f = open(alnFile)
	h = f.readline()
	for line in f:
		line = line.rstrip()
		spe, seq = line.split()
		print('>%s\n%s' % (spe, seq))

if __name__ == '__main__':
	main()

