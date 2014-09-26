#!/usr/bin/env python3

import sys
import fractions
sys.path.insert(0, '../common/python/')

import primality


def main():
    max_ = 12000

    count = 0
    for d in range(5, max_ + 1):
        for n in range(1, d):
            if 2*n >= d:
                break
            if 3*n <= d:
                continue
            if fractions.gcd(n, d) == 1:
                count += 1
    print(count)


if __name__ == '__main__':
    main()
