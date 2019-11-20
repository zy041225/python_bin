#!/usr/bin/perl -w
use strict;

use strict;
use warnings;
use Bio::EnsEMBL::Registry;
Bio::EnsEMBL::Registry->load_registry_from_db(
	-host => 'ensembldb.ensembl.org',
	-user => 'anonymous'
);

die "perl $0 <ENSR_ID>" unless(@ARGV == 1);

my $regulatory_feature_adaptor = Bio::EnsEMBL::Registry->get_adaptor('Human', 'Funcgen', 'RegulatoryFeature');
#my $regulatory_feature_demo_stable_id = $ARGV[0];
my $regulatory_feature_demo_stable_id = 'ENSR00000165384';
#my $regulatory_feature_demo_stable_id = "ENSR00000070143";
#die $regulatory_feature_demo_stable_id;

my $regulatory_feature = $regulatory_feature_adaptor->fetch_by_stable_id($regulatory_feature_demo_stable_id);
print "The regulatory feature with stable id: "  . $regulatory_feature->stable_id . " has the following activities: \n";

my $regulatory_activity_adaptor = Bio::EnsEMBL::Registry->get_adaptor('homo_sapiens', 'funcgen', 'RegulatoryActivity');
my $regulatory_activity_list    = $regulatory_activity_adaptor->fetch_all_by_RegulatoryFeature($regulatory_feature);

foreach my $current_regulatory_activity (@$regulatory_activity_list) {
	print "\tIn the epigenome "  
	. $current_regulatory_activity->get_Epigenome->display_label 
	. ' it is: ' 
	. $current_regulatory_activity->activity 
	. "\n";
}

