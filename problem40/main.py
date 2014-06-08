#!/usr/bin/env python3

from operator import mul
from functools import reduce


def main():
    s = ''.join(str(i) for i in range(1, 1000001))
    nums = [int(s[(10**i)-1]) for i in range(7)]
    print(reduce(mul, nums, 1))


if __name__ == '__main__':
    main()
