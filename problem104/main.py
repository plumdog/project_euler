#!/usr/bin/env python3

import itertools


DIGITS = set('123456789')
LEN_DIGITS = len(DIGITS)
MAX_WITH_DIGITS = 10**LEN_DIGITS


def main():
    f_prev = 0
    f = 1

    for n in itertools.count(2):
        f, f_prev = f + f_prev, f

        if start_and_end_pandigital(f):
            print(n)
            return


def start_and_end_pandigital(num):
    if num < MAX_WITH_DIGITS:
        return False
    if set(str(num % MAX_WITH_DIGITS)) == DIGITS:
        str_ = str(num)
        return set(str_[:LEN_DIGITS]) == DIGITS


if __name__ == '__main__':
    main()
