#!/usr/bin/python3

def get_log(indir):
	import os
	import re
	import sys

	for file in os.listdir(indir):
		if file.endswith('.sh'):
			file = os.path.join(indir, file)
			f = open(file)
			content = f.read()
			f.close()
			match = re.findall(r'-o\s+(\S+\.bam)', content)
			bamFile = match[0]
			path = os.path.dirname(bamFile)
			for log in os.listdir(indir):
				log = os.path.join(indir, log)
				if log.startswith(file + '.e'):
					os.system('cp %s %s/hisat2.sh.log' % (log, path))

def main():
	import sys
	
	if len(sys.argv) != 2:
		sys.exit('python3 %s <log_dir>' % (sys.argv[0]))
	
	get_log(sys.argv[1])	

if __name__ == '__main__':
	main()

