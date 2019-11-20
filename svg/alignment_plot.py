#!/usr/bin/env python3

def plot_backbond(p, length, scale):
	import svgwrite
	shape = p.add(p.g(id = 'backbond', fill = 'black', stroke = 'black', stroke_width = 1))
	l = length/scale
	shape.add(p.rect(insert = (5, 5), size = (l, 5)))
	return p

def plot_bed(p, bedFile, scale):
	import svgwrite
	shape = p.add(p.g(id = 'aln'))
	
	x = 5
	y = 11

	with open(bedFile) as f:
		for line in f:
			line = line.rstrip()
			tmp = line.split('\t')
			bg = int(tmp[1])
			ed = int(tmp[2])
			color = tmp[6]
			start = x + bg/scale
			l = (ed-bg)/scale
			shape.add(p.rect(insert = (start, y), size = (l, 2), fill = 'rgb(%s)' % color))
			y += 2

	return p

def main():
	import sys
	import svgwrite
	if len(sys.argv) != 5:
		sys.exit('python3 %s <scaffold_length> <alignment.bed> <scale> <out.svg>' % (sys.argv[0]))

	length = int(sys.argv[1])
	bedFile = sys.argv[2]
	scale = float(sys.argv[3])
	outFile = sys.argv[4]

	p = svgwrite.Drawing(outFile)
	p = plot_backbond(p, length, scale)
	p = plot_bed(p, bedFile, scale)

	p.save()

if __name__ == '__main__':
	main()

