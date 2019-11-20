#!/usr/bin/python3

# modify from https://stackoverflow.com/questions/35315873/python-3-travel-directory-tree-with-limited-recursion-depth
def iterate_walk(top, maxdepth):
	import os
	dirs, nondirs = [], []
	for name in os.listdir(top):
		if os.path.isdir(os.path.join(top, name)):
			dirs.append(name)
		else:
			nondirs.append(name)
		#(dirs if os.path.isdir(os.path.join(top, name)) else nondirs).append(name)
	yield top, dirs, nondirs
	if maxdepth > 1:
		for name in dirs:
			for x in iterate_walk(os.path.join(top, name), maxdepth-1):
				yield x

def specific_walk(top, depth):
	import os
	dirs, nondirs = [], []
	for name in os.listdir(top):
		if os.path.isdir(os.path.join(top, name)):
			dirs.append(name)
		else:
			nondirs.append(name)
	if depth == 1:
		yield top, dirs, nondirs
	else:
		for name in dirs:
			for x in specific_walk(os.path.join(top, name), depth-1):
				yield x

def main():
	import sys

	if len(sys.argv) != 3:
		sys.exit('python3 %s <dir> <maxdepth>' % (sys.argv[0]))
	
	indir = sys.argv[1]
	maxdepth = int(sys.argv[2])

	for x in iterate_walk(indir, maxdepth):
		print(x)
	print('###')

	for x in specific_walk(indir, maxdepth):
		print(x)

if __name__ == '__main__':
	main()

