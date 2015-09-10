#!/usr/bin/env python3

import sys
sys.path.insert(0, '../../common/python/')

from itertools import count
from functools import lru_cache

from primality import prime_factors as prime_factors_


@lru_cache(maxsize=None)
def prime_factors(num):
    return prime_factors_(num)


def main():
    for i in count(1):
        if (len(prime_factors(i)) >= 4) and \
           (len(prime_factors(i+1)) >= 4) and \
           (len(prime_factors(i+2)) >= 4) and \
           (len(prime_factors(i+3)) >= 4):
            print(i)
            return


if __name__ == '__main__':
    main()
