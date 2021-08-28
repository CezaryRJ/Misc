use strict;
use LWP::UserAgent;

#open a connection and fetch the site
my $ua = new LWP::UserAgent;
$ua->timeout(120);
my $url='https://www.nordrefollo.kommune.no/nyheter/ ';
my $request = new HTTP::Request('GET', $url); #fetch
my $response = $ua->request($request);
my $content = $response->content();#get content

$a = 0;#counter

#/[0-9][0-9]\.06\.[0-9][0-9][0-9][0-9]/g  <--this regex also works

while($content =~ /\/juni\//g){#count matches
	$a++;
}

print $a;#print matches
