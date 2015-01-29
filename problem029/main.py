#!/usr/bin/env python3

from itertools import product

print(len({a**b for (a, b) in product(range(2, 101), range(2, 101))}))
