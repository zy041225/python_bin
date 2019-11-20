#!/usr/bin/python3

def main():
	import sys
	if len(sys.argv) != 2:
		sys.exit('python3 %s <aln>' % (sys.argv[0]))

	alnFile = sys.argv[1]

	f = open(alnFile)
	h = f.readline()
	n = 0
	l = 0
	out = ''
	for line in f:
		n += 1
		line = line.rstrip()
		spe, seq = line.split()
		l = len(seq)
		out += '\n' + line
	
	out = '   %i   %i' % (n, l) + out
	print(out)

if __name__ == '__main__':
	main()

