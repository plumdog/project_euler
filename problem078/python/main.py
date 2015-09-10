#!/usr/bin/env python3

import itertools
import math

MOD = 1000000
CACHE = {}


def main():
    for i in itertools.count(1):
        if num_piles(i) % MOD == 0:
            print(i)
            return


def num_piles(num):
    global CACHE

    if num < 0:
        return 0
    if num <= 1:
        return 1
    if num == 2:
        return 2

    try:
        return CACHE[num]
    except KeyError:
        pass

    total = 0
    # n - k(3k-1)/2 > 0
    # 2n - k(3k-1) > 0
    # 2n - 3k^2 + k > 0
    # 3k^2 - k - 2n < 0
    # k^2 - k/3 - 2n/3 < 0
    # (k - 1/6)^2 < 1/36 + 2n/3
    # k < 1/6 +/- (1/36 + 2n/3)^0.5

    max_ = math.ceil(1/6 + math.sqrt(1/36 + 2*num/3))
    min_ = math.floor(1/6 - math.sqrt(1/36 + 2*num/3))

    for k in range(min_, max_ + 1):
        if k == 0:
            continue
        term = num - (k*(3*k-1)) // 2
        if term < 0:
            continue
        value = num_piles(term)
        if k % 2 == 0:
            total -= value % MOD
        else:
            total += value % MOD

    CACHE[num] = total
    return total


if __name__ == '__main__':
    main()
