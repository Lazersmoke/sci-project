use strict;
use 5.010;
use warnings;
my $x = 0;
my @array = (1 .. 1000000);
foreach my $element (@array) {
    $x+=5;
}
print "$x\n";
