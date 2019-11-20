args = commandArgs(T)

library(DESeq2)

contsTab = read.delim(args[1])
desi = read.table(args[2])

dds = DESeqDataSetFromMatrix(contsTab,desi,design =~ tissue)
dds = DESeq(dds,test="LRT",reduced = ~ 1)
res = results(dds)
write.table(res, args[3], sep="\t", quote = F)

