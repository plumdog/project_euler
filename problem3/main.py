#!/usr/bin/env python3

import math
from functools import lru_cache

NUM = 600851475143

@lru_cache(maxsize=None)
def is_prime(num):
    top = int(math.floor(math.sqrt(num)))
    for i in range(2, top + 1):
        if num % i == 0:
            return False
    return True

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
