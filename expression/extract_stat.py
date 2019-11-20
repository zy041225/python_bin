#!/usr/bin/python3

def extract(log):
	f = open(log)
	content = f.read()

	import re
	import sys

	total_m = re.findall(r'(\d+)\s+reads; of these:', content)
	total_num = int(total_m[0])

	unpair_m = re.findall(r'(\d+)\s+\(\d+\.\d+\%\)\s+were unpaired; of these:', content)
	if unpair_m:
		unpair_num = int(unpair_m[0])
	else:
		unpair_num = 0

	no_m = re.findall(r'(\d+)\s+\(\d+\.\d+%\)\s+aligned 0 times', content)
	no_num = int(no_m[0])

	uniq_m = re.findall(r'(\d+)\s+\(\d+\.\d+%\)\s+aligned exactly 1 time', content)
	uniq_num = int(uniq_m[0])
	
	mul_m = re.findall(r'(\d+)\s+\(\d+\.\d+%\)\s+aligned \>1 times', content)
	mul_num = int(mul_m[0])

	return total_num, unpair_num, no_num, uniq_num, mul_num

'''
#single end
35140545 reads; of these:
	35140545 (100.00%) were unpaired; of these:
		10080041 (28.68%) aligned 0 times
		19173310 (54.56%) aligned exactly 1 time
		5887194 (16.75%) aligned >1 times
71.32% overall alignment rate

#pair end
29919978 reads; of these:
	29919978 (100.00%) were paired; of these:
		14245124 (47.61%) aligned concordantly 0 times
		9611880 (32.13%) aligned concordantly exactly 1 time
		6062974 (20.26%) aligned concordantly >1 times
		----
		14245124 pairs aligned concordantly 0 times; of these:
			551590 (3.87%) aligned discordantly 1 time
		----
		13693534 pairs aligned 0 times concordantly or discordantly; of these:
			27387068 mates make up the pairs; of these:
				18721778 (68.36%) aligned 0 times
				5585975 (20.40%) aligned exactly 1 time
				3079315 (11.24%) aligned >1 times
68.71% overall alignment rate
'''

def main():
	import sys

	if len(sys.argv) != 2:
		sys.exit('python3 %s <hisat2.sh.log>' % (sys.argv[0]))

	total_num, unpair_num, no_num, uniq_num, mul_num = extract(sys.argv[1])

	import os
	sample = os.path.dirname(sys.argv[1])
	sample = sample.split('/')[-1]

	print('%s\t%i\t%i\t%.2f\t%i\t%.2f\t%i\t%.2f\t%i\t%.2f' % (sample, total_num, unpair_num, unpair_num/total_num*100, no_num, no_num/total_num*100, uniq_num, uniq_num/total_num*100, mul_num, mul_num/total_num*100))

if __name__ == '__main__':
	main()



