#!/usr/bin/env python3

import sys
sys.path.insert(0, '../common/python/')
import math

from primality import is_prime

NUM = 600851475143


def main():
    top = int(math.floor(math.sqrt(NUM)))
    largest_prime_factor = None

    for i in range(2, top + 1):
        if NUM % i == 0:
            if is_prime(i):
                largest_prime_factor = i

    print(largest_prime_factor)


if __name__ == '__main__':
    main()
