#!/usr/bin/env python3

from collections import namedtuple
from fractions import Fraction


def u_n(n):
    return 1 - n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7 + n**8 - n**9 + n**10


Point = namedtuple('Point', 'x y')


def main():
    total = 0
    for i in range(1, 11):
        values = [Point(j, u_n(j)) for j in range(1, i + 1)]
        next_x = i + 1

        # Use Langrange polynomial so that we can find the next value
        # without solving for the polynomial directly.
        next_value = 0

        for k in range(len(values)):
            top_prod = 1
            bottom_prod = 1

            for j in range(len(values)):
                if j == k:
                    continue
                top_prod *= (next_x - values[j].x)
                bottom_prod *= (values[k].x - values[j].x)
            next_value += values[k].y * Fraction(top_prod / bottom_prod)
        total += next_value
    print(total)


if __name__ == '__main__':
    main()
