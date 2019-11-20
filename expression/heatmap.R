args = commandArgs(T)

dat = read.table(args[1], h=T, row.names = 1)
pdf(args[2])

heatmap(as.matrix(dat))

