#!/usr/bin/env python3

import itertools
print(max(sum(int(ch) for ch in str(a**b)) for a, b in itertools.product(range(1, 100), range(1, 100))))
