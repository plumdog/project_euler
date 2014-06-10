#!/usr/bin/env python3

import sys
sys.path.insert(0, '../common/python/')

import itertools
from operator import mul
from functools import reduce

from primality import prime_factors

NUM = 500


def triangle(num):
    return num * (num + 1) // 2


def first_tr_with_divisors(num):
    for i in itertools.count():
        tr = triangle(i)
        if divisors_count(tr) > num:
            return tr


def divisors_count(i):
    return reduce(mul, [j + 1 for j in prime_factors(i).values()], 1)


if __name__ == '__main__':
    print(first_tr_with_divisors(NUM))
