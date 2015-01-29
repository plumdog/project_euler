#!/usr/bin/env python3

import sys
sys.path.insert(0, '../common/python/')

from primality import prime_sieve
import math

MAX = 50000000
#MAX = 50

def main():
    primes = sorted(prime_sieve(int(math.sqrt(MAX))))
    nums = set()

    for p1 in primes:
        for p2 in primes:
            for p3 in primes:
                val = power_combine(p1, p2, p3)
                if val < MAX:
                    nums.add(val)
                else:
                    break
    print(len(nums))

def power_combine(p1, p2, p3):
    return p1**2 + p2**3 + p3**4

if __name__ == '__main__':
    main()
