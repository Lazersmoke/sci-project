use strict;
use 5.010;
use warnings;
my $x = 0.0;
my $y = 0.1;
while ($y<500000.1){
    $x+=0.1;
    $y+=0.1;
}
print "$x\n";
