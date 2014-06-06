#!/usr/bin/env python3

import math
import itertools
from collections import defaultdict
from operator import mul
from functools import reduce

NUM = 500

def prime_factors(num):
    if num <= 1:
        return defaultdict(int)

    prime_divs = defaultdict(int)

    trial = 2
    num_ = num
    top = int(math.sqrt(num_))

    while True:
        if trial > top:
            d = defaultdict(int)
            d[num_] = 1
            return d

        if num_ % trial == 0:
            parent = prime_factors(num_ // trial)
            parent[trial] += 1
            return parent
        else:
            if trial == 2:
                trial += 1
            else:
                trial += 2


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
