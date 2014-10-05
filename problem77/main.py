#!/usr/bin/env python3

import sys
sys.path.insert(0, '../common/python/')

from primality import prime_sieve

import collections
import functools
import itertools

def main():
    max_ = 5000
    primes = prime_sieve(100)

    for total in itertools.count(2):
        ways = collections.defaultdict(int)
        ways[0] = 1

        for first_num in primes:
            for way in range(first_num, total+1):
                ways[way] += ways[way - first_num]
        if ways[total] > max_:
            print(total)
            return


if __name__ == '__main__':
    main()
