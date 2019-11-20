#!/usr/bin/perl -w
use strict;

die "perl $0 <indir>" unless @ARGV == 1;

my@file=glob "$ARGV[0]/part*/part*.num";
my $rpka=0;
my %rpks;

foreach my$ele(@file){
	open IN,"$ele";
	while(<IN>){
		chomp;
		my@A=split(/\t/);
		$rpks{$A[0]}{'num'}=$A[1];
		$rpks{$A[0]}{'len'}=$A[2];
		$rpks{$A[0]}{'rpk'}=($rpks{$A[0]}{num}/$rpks{$A[0]}{len})*1000;
		$rpka+=$rpks{$A[0]}{'rpk'};
	}
	close IN;
}

foreach my$key(keys %rpks){
	my $tpm=sprintf "%.4f", ($rpks{$key}{'rpk'}*1000000)/$rpka;
	my $o = sprintf "%.4f", $rpka;
	print "$key\t$tpm\t$o\t$rpks{$key}{'num'}\t$rpks{$key}{'len'}\n";
}

