#!/usr/bin/env python3

import decimal
import math


DIGITS = 100
decimal.getcontext().prec = DIGITS + 10
EPS = decimal.Decimal(10)**-(DIGITS + 5)


def main():
    digits_total = 0

    for i in range(2, DIGITS):
        if not is_square(i):
            sqrt = find_sqrt(i)
            digits_total += sum_digits(sqrt)
    print(digits_total)


def find_sqrt(num):
    return interval_bisect(decimal.Decimal(0), decimal.Decimal(num), decimal.Decimal(num))


def is_square(num):
    sqrt = math.sqrt(num)
    return int(sqrt)**2 == num


def interval_bisect(bottom, top, value):
    mid = (bottom + top) / 2
    mid_value = mid**2

    if abs(value - mid_value) < EPS:
        return mid

    if mid_value > value:
        return interval_bisect(bottom, mid, value)
    else:
        return interval_bisect(mid, top, value)


def sum_digits(num):
    total = 0
    digits = [str(i) for i in range(10)]
    digits_found = 0
    for digit in str(num):
        if digit in digits:
            digits_found += 1
            total += int(digit)
        if digits_found >= DIGITS:
            break
    return total


if __name__ == '__main__':
    main()
