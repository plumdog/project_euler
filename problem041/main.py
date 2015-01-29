#!/usr/bin/env python3

import sys
sys.path.insert(0, '../common/python/')

from primality import is_prime
from itertools import permutations


def main():
    # n is the number of digits. For sum numbers of digits, the sum of
    # the digits is a multiple of 3, so there are never any divisors.
    # 1..2 = 3
    # 1..3 = 6
    # 1..5 = 15
    # 1..6 = 21
    # 1..8 = 36
    # 1..9 = 45
    #
    # And we can skip 1 digit, because we know 7 is the largest
    # possible, and that's what we set maxprime to start with.
    maxprime = 7
    for n in [4, 5, 7]:
        for digits in permutations(range(1, n + 1)):
            num = int(''.join(str(i) for i in digits))
            if (num > maxprime) and is_prime(num):
                maxprime = num
    print(maxprime)


if __name__ == '__main__':
    main()
