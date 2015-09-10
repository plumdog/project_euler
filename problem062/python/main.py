#!/usr/bin/env python3

import itertools
import collections


def main():
    digits_count = collections.defaultdict(set)
    num = 5
    power = 3
    for i in itertools.count():
        calc = i**power
        val = int(''.join(sorted(str(calc), reverse=True)))
        digits_count[val].add(calc)
        if len(digits_count[val]) == num:
            print(min(digits_count[val]))
            return

if __name__ == '__main__':
    main()
