#!/usr/bin/env python3
import sys
from draw_aln import read_aln, get_aln_range
import svgwrite

def draw_backbone(scaf, start, end, scale, d, leftmost, topmost, axis, col='black', label=True):
	if axis == 'x':
		x1 = leftmost
		x2 = x1+(end-start+1)/scale
		y1 = topmost
		y2 = topmost
		xmid = (x1+x2)/2
		ymid = (y1+y2)/2
		if label: d.add(d.text(scaf, insert = (xmid, ymid-5), font_size = 8, font_family = 'Arial'))
	elif axis == 'y':
		x1 = leftmost
		x2 = leftmost
		y1 = topmost
		y2 = y1+(end-start+1)/scale
		xmid = (x1+x2)/2
		ymid = (y1+y2)/2
		if label: d.add(d.text(scaf, insert = (xmid-5, ymid), font_size = 8, font_family = 'Arial'))
	d.add(d.line(start = (x1, y1), end = (x2, y2), stroke = col, stroke_width = 1))

	loc = [x1, y1, start, end]

	return d, loc


def draw_dotplot(aln_list, d, scale, leftmost1, topmost1, leftmost2, topmost2, ort1='+', ort2='+', bg1='NA', ed1='NA', bg2='NA', ed2='NA'):
	rang1, rang2 = get_aln_range(aln_list)

	xloc1 = leftmost1
	yloc1 = topmost1
	scaf1 = rang1[0]
	if bg1 == 'NA':
		bg1, ed1 = rang1[1:]
	l = (ed1-bg1+1)/scale
	#d.add(d.line(start = (xloc1, yloc1), end = (xloc1+l, yloc1), stroke = 'black', stroke_width = 1))
	
	xloc2 = leftmost2
	yloc2 = topmost2
	scaf2 = rang2[0]
	if bg2 == 'NA':
		bg2, ed2 = rang2[1:]
	l = (ed2-bg2+1)/scale
	#d.add(d.line(start = (xloc2, yloc2), end = (xloc2, yloc2+l), stroke = 'black', stroke_width = 1))

	for info in aln_list:
		scaf1, strand1, start1, end1, scaf2, strand2, start2, end2, color = info
		
		if end1 < bg1 or start1 > ed1 or end2 < bg2 or start2 > ed2:
			continue
		
		if ort1 == '+':
			x1 = xloc1+(start1-bg1+1)/scale
			x2 = xloc1+(end1-bg1+1)/scale
		else:
			x1 = xloc1+(ed1-start1+1)/scale
			x2 = xloc1+(ed1-end1+1)/scale

		if ort2 == '+':
			y1 = yloc2+(start2-bg2+1)/scale
			y2 = yloc2+(end2-bg2+1)/scale
		else:
			y1 = yloc2+(ed2-start2+1)/scale
			y2 = yloc2+(ed2-end2+1)/scale
		
		d.add(d.line(start = (x1, y1), end = (x2, y2), stroke = 'black', stroke_width = 1))
	
	return d		

def main():
	if len(sys.argv) != 4:
		sys.exit('python3 %s <aln> <scale> <out.svg>' % (sys.argv[0]))
		
	alnFile = sys.argv[1]
	scale = int(sys.argv[2])
	outFile = sys.argv[3]

	aln_dict = read_aln(alnFile)

	d = svgwrite.Drawing(outFile)
	leftmost1 = 25
	topmost1 = 25
	leftmost2 = 25
	topmost2 = 25
	
	for key in aln_dict:
		d = draw_dotplot(aln_dict[key], d, scale, leftmost1, topmost1, leftmost2, topmost2)

	d.save()

if __name__ == '__main__':
	main()

