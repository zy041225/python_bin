#!/usr/bin/python3
import sys
#sys.path.append('/hwfssz1/ST_DIVERSITY/PUB/USER/zhouyang/python_bin/svg/')

from draw_gene import draw_gene_v1, read_gff_v1, draw_gene_model
from draw_aln import draw_aln, read_aln
from draw_backbone import draw_backbone

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
			row = tmp[0]
			id = tmp[1]
			if row not in gene: gene[row] = []
			gene[row].append(id)
		elif flag == 2:
			row1, row2, scaf1, scaf2, ort1, ort2 = line.split('\t')[:]
			row1 = int(row1)
			row2 = int(row2)
			aln.append([row1, row2, scaf1, scaf2, ort1, ort2])
			if scaf1 not in orient:
				orient[scaf1] = ort1
			elif orient[scaf1] != ort1:
				sys.exit('Error: conflict in %s orientation in [range], please check\n' % (scaf1))
			if scaf2  not in orient:
				orient[scaf2] = ort2
			elif orient[scaf2] != ort2:
				sys.exit('Error: conflict in %s orientation in [range], please check\n' % (scaf2))
		elif flag == 3:
			row, scaf, start, end = line.split('\t')[:]
			start = int(start)
			end = int(end)
			if row not in rang: rang[row] = []
			rang[row].append([scaf, start, end])

	return gene, aln, rang, orient

def main():
	import sys
	import svgwrite

	if len(sys.argv) <= 7:
		sys.exit('python3 %s <conf> <gff> <aln> <scale> <outfile> <type[gene|gene_model]> <arrow[1|0]>' % (sys.argv[0]))

	conf = sys.argv[1]
	gff = sys.argv[2]
	file = sys.argv[3]
	scale = int(sys.argv[4])
	outfile = sys.argv[5]
	typ = sys.argv[6]
	arrow_flag = 1
	if len(sys.argv) == 8:
		arrow_flag = sys.argv[7]

	if typ != 'gene' and typ != 'gene_model':
		sys.exit('python3 %s <conf> <gff> <aln> <scale> <outfile> <type[gene|gene_model]>' % (sys.argv[0]))

	gene_order, aln_order, rang, orient = read_conf(conf)
	gene_dict, cds_dict = read_gff_v1(gff)
	
	aln_dict = read_aln(file)

	d = svgwrite.Drawing(outfile)

	x = 25
	y = 25
	loc = {}

	for row in rang:
		x = 25
		for info in rang[row]:
			scaf, start, end = info[:]
			
			d, location = draw_backbone(scaf, start, end, scale, d, x, y)
			loc[scaf] = location

			x += (end-start+1)/scale+20+25
		y += 50
	

	for info in aln_order:
		row1, row2, scaf1, scaf2, ort1, ort2 = info[:]
		lm1, tm1, bg1, ed1 = loc[scaf1][:]
		lm2, tm2, bg2, ed2 = loc[scaf2][:]
		key = '%s#%s' % (scaf1, scaf2)
		d = draw_aln(aln_dict[key], d, scale, lm1, tm1, lm2, tm2, ort1=ort1, ort2=ort2, bg1=bg1, ed1=ed1, bg2=bg2, ed2=ed2)


	for row in sorted(gene_order.keys()):
		x = 0
		for id in gene_order[row]:
			scaf = gene_dict[id][0]
			ort = orient[scaf]
			x, y, bg, ed = loc[scaf][:]
			if typ == 'gene_model':
				d = draw_gene_model(cds_dict[id], id, d, scale, x, y, ort=ort, bg=bg, ed=ed)
			elif typ == 'gene':
				d = draw_gene_v1(gene_dict[id], id, d, scale, x, y, ort=ort, bg=bg, ed=ed, arrow=arrow_flag)
		y += 50

	d.save()

if __name__ == '__main__':
	main()

