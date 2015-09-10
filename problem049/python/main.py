#!/usr/bin/env python3

import sys
sys.path.insert(0, '../../common/python/')

from primality import is_prime
from itertools import permutations


def int_permutations(num):
    for perm in permutations(str(num)):
        out = int(''.join(perm))
        if out > num:
            yield out


def main():
    for a in range(1000, 10000):
        if a == 1487:
            continue

        perms = list(int_permutations(a))
        for b in perms:
            c = a + 2*(b - a)
            seq = (a, b, c)
            if c in perms and all(is_prime(x) for x in seq):
                print(''.join(str(x) for x in seq))
                return


if __name__ == '__main__':
    main()
