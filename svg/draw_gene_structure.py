#!/usr/bin/python3

def read_gff(gff):
	import sys
	import re

	f = open(gff)

	id = ''
	gene_dict = {}
	cds_dict = {}

	for line in f:
		tmp = line.split('\t')
		scaf = tmp[0]
		start = int(tmp[3])
		end = int(tmp[4])
		strand = tmp[6]
		
		if tmp[2] == 'mRNA':
			m = re.search(r'^ID=(\S+?);', tmp[8])
			id = m.group(1)
			
			if scaf not in gene_dict: gene_dict[scaf] = []

			gene_dict[scaf].append([id, start, end, strand])
		else:
			m = re.search(r'^Parent=(\S+?);', tmp[8])
			if m.group(1) != id:
				sys.exit('error: \nID: %s\n%s' % (id, line))
			
			if id not in cds_dict: cds_dict[id] = []
			cds_dict[id].append([scaf, start, end, strand])

	return gene_dict, cds_dict

def get_range(gene_dict):
	pos = {}
	for scaf in sorted(gene_dict.keys()):
		for info in sorted(gene_dict[scaf], key = lambda x: x[1]):
			id, start, end, strand = info[:]
			if scaf in pos:
				if start < pos[scaf][0]: pos[scaf][0] = start
				if end > pos[scaf][1]: pos[scaf][1] = end
			else:
				pos[scaf] = [start, end]
	return pos

def get_path(xloc, yloc, start, bg, end, scale, strand, l):
	path_x = 0
	path_y = 0
	h = 0
	l_x = 0
	l_y = 0
	if strand == '+':
		path_x = xloc + (start-bg+1)/scale
		path_y = yloc
		h = 0.8*l
		l_x = 0.2*l
		l_y = 6
	else:
		path_x = xloc + (end-bg+1)/scale
		path_y = yloc
		h = -0.8*l
		l_x = -0.2*l
		l_y = 6
	return path_x, path_y, h, l_x, l_y

def draw_gene(gene_dict, d, scale, leftmost, topmost):
	import svgwrite
	import sys

	pos = get_range(gene_dict)

	xloc = leftmost
	yloc = topmost
	for scaf in sorted(gene_dict.keys()):
		bg, ed = pos[scaf][:]
		l = (ed-bg+1)/scale
		# draw backbone and scaf ID
		d.add(d.line(start = (xloc-20, yloc), end = (xloc+l+20, yloc), stroke = 'rgb(0,0,0)', stroke_width = 1))
		d.add(d.text(scaf, insert = (xloc-5, yloc), font_size = 8, fill = 'black', font_family = 'Arial'))

		for info in sorted(gene_dict[scaf], key = lambda x: x[1]):
			id, start, end, strand = info[:]
			l = (end-start+1)/scale
			# draw gene and gene ID
			d.add(d.text(id, insert = (xloc-5, yloc), font_size = 8, fill = 'black', font_family = 'Arial'))
			path_x, path_y, h, l_x, l_y = get_path(xloc, yloc, start, end, bg, scale, strand, l)
			d.add(d.path('M%f %f v -3 h %f v -3 l %f %f M%f %f v 3 h %f v 3 l %f -%f' % (path_x, path_y, h, l_x, l_y, path_x, path_y, h, l_x, l_y), fill = 'red', stroke = 'black'))
		
		yloc += 30
	return d

def draw_gene_exons(cds_dict, d, scale, leftmost, topmost):
	import svgwrite
	import sys

	xloc = leftmost
	yloc = topmost
	for id in cds_dict:
		sort_info = sorted(cds_dict[id], key = lambda x: x[1])
		bg = sort_info[0][1]
		ed = sort_info[-1][2]
		l = (ed-bg+1)/scale
		scaf = sort_info[0][0]
		# draw backbone and gene ID
		d.add(d.line(start = (xloc-20, yloc), end = (xloc+l+20, yloc), stroke = 'rgb(0,0,0)', stroke_width = 1))
		d.add(d.text(scaf, (xloc-25, yloc-15), font_size = 8, fill = 'black', font_family = 'Arial'))
		d.add(d.text(id, (xloc-5, yloc-5), font_size = 8, fill = 'black', font_family = 'Arial'))

		count = 0
		for info in cds_dict[id]:
			count += 1
			scaf, start, end, strand = info[:]
			l = (end-start+1)/scale
			x = (start-bg+1)/scale+xloc
			y = yloc-5

			# draw CDS
			## draw the first CDS in mRNA
			tri_y1, tri_y2, tri_y3 = yloc, yloc+10, yloc-10
			tri_x1, tri_x2, tri_x3 = 0, 0, 0
			if strand == '+':
				tri_x1 = x+l
				tri_x2 = x
				tri_x3 = x
				if count == len(cds_dict[id]): 
					d.add(d.polygon(points = ((tri_x1, tri_y1), (tri_x2, tri_y2), (tri_x3, tri_y3)), fill = 'red', stroke = 'black', stroke_width = 0.5))
					continue
			elif strand == '-':
				tri_x1 = x
				tri_x2 = x+l
				tri_x3 = x+l
				if count == 1:
					d.add(d.polygon(points = ((tri_x1, tri_y1), (tri_x2, tri_y2), (tri_x3, tri_y3)), fill = 'red', stroke = 'black', stroke_width = 0.5))
					continue
			## draw the remaining CDS
			d.add(d.rect(insert = (x, y), size = (l, 10), fill = 'red', stroke = 'black', stroke_width = 0.5))
		yloc += 30

	return d

def main():
	import sys
	import svgwrite

	if len(sys.argv) != 4:
		sys.exit('python3 %s <gff> <gene|exon> <scale>' % (sys.argv[0]))
	elif sys.argv[2] != 'gene' and sys.argv[2] != 'exon':
		sys.exit('python3 %s <gff> <gene|exon> <scale>\n## please specify drawing type' % (sys.argv[0]))

	gff = sys.argv[1]
	typ = sys.argv[2]
	scale = int(sys.argv[3])

	gene_dict, cds_dict = read_gff(gff)
	d = svgwrite.Drawing('tmp.svg')

	leftmost = 25
	topmost = 25

	if typ == 'gene':
		d = draw_gene(gene_dict, d, scale, leftmost, topmost)
	elif typ == 'exon':
		d = draw_gene_exons(cds_dict, d, scale, leftmost, topmost)

	d.save()

if __name__ == '__main__':
	main()

