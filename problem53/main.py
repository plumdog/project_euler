#!/usr/bin/env python3

from functools import lru_cache
import math


@lru_cache(maxsize=None)
def factorial(n):
    return math.factorial(n)


def choose(n, r):
    return factorial(n) / (factorial(r) * factorial(n-r))


def main():
    max_ = 1000000
    upto = 100
    count = 0
    for n in range(1, upto+1):
        for r in range(n):
            if choose(n, r) > max_:
                count += 1
    print(count)


if __name__ == '__main__':
    main()
