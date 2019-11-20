#!/usr/bin/python3
import sys
#sys.path.append('/hwfssz1/ST_DIVERSITY/PUB/USER/zhouyang/python_bin/svg/')

from draw_gene import draw_gene_v2, read_gff_v1, draw_gene_model
from draw_aln import read_aln
from dotplot import draw_backbone, draw_dotplot

def read_conf(conf):
	f = open(conf)

	gene = {}
	aln = []
	rang = {}
	flag = 0
	orient = {}

	for line in f:
		if line[0] == '#': continue
		if line[0] == '\n': continue
		line = line.rstrip()
		if line == '[gene]':
			flag = 1
			continue
		elif line == '[aln]':
			flag = 2
			continue
		elif line == '[range]':
			flag = 3
			continue

		if flag == 1:
			tmp = line.split('\t')
			axis = tmp[0]
			if axis != 'x' and axis != 'y':
				sys.exit('Error: gene axis should be x or y: %s\n' % (line))
			id = tmp[1]
			if axis not in gene: gene[axis] = []
			gene[axis].append(id)
		elif flag == 2:
			axis1, axis2, scaf1, scaf2, ort1, ort2 = line.split('\t')[:]
			if axis1 != 'x' or axis2 != 'y':
				sys.exit('Error: alignment axis should be first x and second y: %s\n' % (line))
			aln.append([axis1, axis2, scaf1, scaf2, ort1, ort2])
			if scaf1 not in orient:
				orient[scaf1] = ort1
			elif orient[scaf1] != ort1:
				sys.exit('Error: conflict in %s orientation in [range], please check\n' % (scaf1))
			if scaf2  not in orient:
				orient[scaf2] = ort2
			elif orient[scaf2] != ort2:
				sys.exit('Error: conflict in %s orientation in [range], please check\n' % (scaf2))
		elif flag == 3:
			axis, scaf, start, end = line.split('\t')[:]
			if axis != 'x' and axis != 'y':
				sys.exit('Error: range axis should be x or y: %s\n' % (line))
			start = int(start)
			end = int(end)
			if axis not in rang: rang[axis] = []
			rang[axis].append([scaf, start, end])

	return gene, aln, rang, orient

def main():
	import sys
	import svgwrite

	if len(sys.argv) != 7:
		sys.exit('python3 %s <conf> <gff> <aln> <scale> <outfile> <type[gene|gene_model]>' % (sys.argv[0]))

	conf = sys.argv[1]
	gff = sys.argv[2]
	file = sys.argv[3]
	scale = int(sys.argv[4])
	outfile = sys.argv[5]
	typ = sys.argv[6]

	if typ != 'gene' and typ != 'gene_model':
		sys.exit('python3 %s <conf> <gff> <aln> <scale> <outfile> <type[gene|gene_model]>' % (sys.argv[0]))

	gene_order, aln_order, rang, orient = read_conf(conf)
	gene_dict, cds_dict = read_gff_v1(gff)
	
	aln_dict = read_aln(file)

	d = svgwrite.Drawing(outfile)

	x = 25
	y = 25
	loc = {}

	for axis in rang:
		x = 25
		y = 25
		for info in rang[axis]:
			scaf, start, end = info[:]
			
			d, location = draw_backbone(scaf, start, end, scale, d, x, y, axis)
			loc[scaf] = location
			
			if axis == 'x':
				x += (end-start+1)/scale+20+25
			elif axis == 'y':
				y += (end-start+1)/scale+20+25

	for info in aln_order:
		axis1, axis2, scaf1, scaf2, ort1, ort2 = info[:]
		lm1, tm1, bg1, ed1 = loc[scaf1][:]
		lm2, tm2, bg2, ed2 = loc[scaf2][:]
		key = '%s#%s' % (scaf1, scaf2)
		d = draw_dotplot(aln_dict[key], d, scale, lm1, tm1, lm2, tm2, ort1=ort1, ort2=ort2, bg1=bg1, ed1=ed1, bg2=bg2, ed2=ed2)

	for axis in sorted(gene_order.keys()):
		x = 0
		for id in gene_order[axis]:
			scaf = gene_dict[id][0]
			ort = orient[scaf]
			x, y, bg, ed = loc[scaf][:]
			if typ == 'gene_model':
				d = draw_gene_model_v2(cds_dict[id], id, d, scale, x, y, ort=ort, bg=bg, ed=ed, axis=axis)
			elif typ == 'gene':
				d = draw_gene_v2(gene_dict[id], id, d, scale, x, y, ort=ort, bg=bg, ed=ed, axis=axis)
		y += 50

	d.save()

if __name__ == '__main__':
	main()

