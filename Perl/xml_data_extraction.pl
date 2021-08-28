use 5.010;
use strict;
use warnings;

use XML::LibXML;

my $filename = 'fil1.xml';

my $file = XML::LibXML->load_xml(location => $filename);#read file with xml parser

foreach my $target ($file->findnodes("//newsitem")) { #find and print
	say 'Headline:    ', $target->findvalue('./headline');
	say 'Story:    ', $target->findvalue('./story');
}