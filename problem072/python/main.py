#!/usr/bin/env python3

import sys
sys.path.insert(0, '../../common/python/')

import primality

max_ = 1000000
print(sum(primality.phi(d) for d in range(2, max_+1)))
