#!/usr/bin/perl

$total = 0;
for $i (1 .. 999) {
    if (($i % 3 == 0) or ($i % 5 == 0)) {
        $total += $i;
    }
}
print "$total\n";
