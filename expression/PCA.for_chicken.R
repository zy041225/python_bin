args = commandArgs(T)

dat = read.table(args[1])
pdf(args[2])

require(psych)
res<-principal(log(dat+1)/log(2),nfactors=12, rotate="varimax")

#for(i in 1:10){
#	plot(res$weights[,i],res$weights[,i],col=c("blue","blue","blue","blue","blue","blue","blue","blue","blue","blue","blue","cyan","cyan","red","red","red","yellow","yellow","yellow","orange","orange","green","green","purple","purple","purple","black","black","black"), pch=19)
#}

for(i in 1:6){
	for(j in (i+1):7){
		plot(res$weights[,i],res$weights[,j],col=c("blue","blue","blue","cyan","cyan","red","red","yellow","yellow","orange","orange","green","green","black","black","black"), pch=19, xlab = i, ylab = j)
		#plot(res$weights[,i],res$weights[,j],col=c("blue","blue","blue","blue","blue","blue","blue","blue","blue","blue","blue","cyan","cyan","red","red","red","yellow","yellow","yellow","orange","orange","green","green","purple","purple","purple","black","black","black"), pch=19)
		text(res$weights[,i], res$weights[,j], labels = row.names(res$weights), cex = 0.7)
	}
}
