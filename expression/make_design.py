#!/usr/bin/python3

def main():
	import sys
	from index import read_info

	for id in sorted(infoDic):
		tissue, sex = id.split('_')[:]
		print('%s\t%s' % (id, tissue))


if __name__ == '__main__':
	main()

