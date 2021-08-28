print "Input parser\n";

#read input  
$parser = <STDIN>;
chomp $parser;
  
  
  
print "Input stage\n";
 
#read input   
$stage = <STDIN>;
chomp $stage;



print "Input sourceid\n";
 
#read input   
$sourceid = <STDIN>;
chomp $sourceid;



print "Input uploaddir\n";
  
#read input  
$uploaddir = <STDIN>;
chomp $uploaddir;



#print input  
print "\n\n\n<Feed vg>\n\n";

print "	parser ", $parser, "\n\n";
print "	stage ", $stage, "\n\n";
print "	sourceid ", $sourceid, "\n\n\n";
print "	uploaddir ", $uploaddir, "\n\n";

print "</Feed vg>\n";