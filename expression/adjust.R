args = commandArgs(T)

library(DESeq2)

countsTab = read.delim(args[1], row.names=1)
cound = colnames(countsTab)
cound = factor(colnames(countsTab))

cds = DESeqDataSetFromMatrix(countsTab, DataFrame(cound), ~cound)
cds = estimateSizeFactors(cds)
write.table(sizeFactors(cds), args[2], sep="\t", quote = F)

