#!/usr/bin/env node
var total = 0;
for (var i = 0; i < 1000; i++) {
    if (i % 3 == 0 || i % 5 == 0) {
        total += i;
    }
}
console.log(total);
