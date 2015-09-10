#!/usr/bin/env python3

from itertools import permutations

print(''.join(str(i) for i in sorted(permutations(range(10)))[999999]))
