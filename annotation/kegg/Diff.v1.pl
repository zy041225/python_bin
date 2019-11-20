#!/usr/bin/perl -w
#use lib '/ifs5/PC_PA_UN/ANIMAL/USER/GROUP2/zhangpei/perl/pm';
use lib '/hwfssz1/ST_DIVERSITY/PUB/USER/zhangpei/perl/pm/';
use TWO_TAB_test;
use Pvalue_adj;
use strict;
use Getopt::Long;
GetOptions(
		'fore=s'=>\our$forefile,
		'back=s'=>\our$backfile,
		'KEGG=s'=>\our$KEGGfile,
		);

die "perl $0 --fore <gene.lst> --back <background.lst> --KEGG all.kegg.gene.tab" unless(defined $forefile && defined $backfile && defined $KEGGfile);

my%fore;
open IN,"$forefile";
while(<IN>){
	chomp;
	my@A=split(/\t/);
	$fore{$A[0]}++;
}
close IN;
my%back;
if($backfile){
	open IN, "$backfile";
	while(<IN>){
		chomp;
		my@A=split(/\t/);
		$back{$A[0]}++;
	}
	close IN;
}
my%KEGG;
my%num;
my%content;
my%all_background;
my$all_background_num=0;
my%all_foreground;
my$all_foreground_num=0;
open IN,"$KEGGfile";
while(<IN>){
	chomp;
	my@A=split(/\t/);
	if(!$all_background{$A[0]}){
		if(!$backfile || ($backfile && $back{$A[0]})){
			$all_background_num++;
			$all_background{$A[0]}++;
		}
	}
	if(!$backfile || ($backfile && $back{$A[0]})){
		$num{$A[3]}{background}++;
	}
	if(!$fore{$A[0]}){next}
	if(!$all_foreground{$A[0]}){
		$all_foreground_num++;
		$all_foreground{$A[0]}++;
	}
	$num{$A[3]}{foreground}++;
	$KEGG{$A[3]}=$A[4];
	$content{$A[3]}[0].=$A[0].",";
	$content{$A[3]}[1].=$A[1].",";
}
close IN;
my%pvalue;
my%strand;
my%num1;
foreach my$key(keys %KEGG){
	my$a=$num{$key}{foreground};
	my$b;
	$b=$num{$key}{background}-$num{$key}{foreground};
	my$c=$all_foreground_num-$num{$key}{foreground};
	my$d;
	$d=$all_background_num-$all_foreground_num-$num{$key}{background}+$num{$key}{foreground};
	if($a<0 || $b<0 || $c<0 || $d<0){die "what in $key!!!\n"}
	$pvalue{$key}=two_tab($a,$b,$c,$d);
	@{$num1{$key}}=($a,$b,$c,$d);
	if($a*$d>$b*$c){
		$strand{$key}="OVER";
	}else{
		$strand{$key}="UNDER";
	}
}
my%qvalue=fdr(%pvalue);
foreach my$key(sort {$qvalue{$a} <=> $qvalue{$b}} keys %qvalue){
	print "$key\t$KEGG{$key}\t$pvalue{$key}\t$qvalue{$key}\t$strand{$key}\t$num{$key}{foreground}\t$num{$key}{background}\t$content{$key}[0]\t$content{$key}[1]\t@{$num1{$key}}\n";
}

