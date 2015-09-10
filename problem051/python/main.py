#!/usr/bin/env python3

import sys
sys.path.insert(0, '../../common/python/')
import itertools
from primality import is_prime


def insert_digit(num, position, digit):
    s = str(num)
    l = len(s)
    return int(s[:l-position] + str(digit) + s[l-position:])


def insert_digits(num, positions, digit):
    for p in positions:
        num = insert_digit(num, p, digit)
    return num


def positions(full_length, pos_length):
    return set(sorted(p for p in itertools.permutations(
        range(full_length), pos_length) if list(sorted(p)) == list(p)))


def main():
    max_base = 1000
    max_num_digits = 4

    for num in range(1, max_base, 2):
        for num_digits in range(1, max_num_digits):
            for pos in positions(len(str(num)) + num_digits, num_digits):
                count = 0
                ps = []
                for digit in range(10):
                    trial = insert_digits(num, pos, digit)
                    if (len(str(trial)) == len(str(num)) + num_digits) \
                       and is_prime(insert_digits(num, pos, digit)):
                        ps.append(trial)
                        count += 1
                if count >= 8:
                    print(min(ps))
                    return


if __name__ == '__main__':
    main()
