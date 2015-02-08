#!/usr/bin/env python3

"""
1/x + 1/y = 1/n
yn + xn = xy
xy - nx - ny = 0
(x - n)(y - n) = n^2
"""

import sys
sys.path.insert(0, '../common/python/')

import primality
import itertools


TARGET = 1000

def main():
    for n in itertools.count(1):
        pfactors_of_n = primality.prime_factors(n)
        num_factors_of_n_sq = 1
        for num in pfactors_of_n.values():
            # This would be *= num + 1 if we were dealing with n, but
            # we're not, we want the number of factors of n^2.
            num_factors_of_n_sq *= (2*num + 1)

        # * 2 because for every solution, we need two factors.
        if num_factors_of_n_sq > TARGET * 2:
            print(n)
            return


if __name__ == '__main__':
    main()
