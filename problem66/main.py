#!/usr/bin/env python3

import math
import fractions
import itertools


def is_square(num):
    sqrt_ = int(math.sqrt(num))
    return sqrt_*sqrt_ == num


def reduce_three(a, b, c):
    """gcd(a, b, c) = gcd(a, gcd(b, c))
    """
    gcd = fractions.gcd(a, fractions.gcd(b, c))
    return a // gcd, b // gcd, c // gcd


class Surd(object):
    """
    represents (b*sqrt(n) + c) / d where b, c, d and n are integers
    """

    def __init__(self, b, c, d, n, *, reduce=True):
        if reduce:
            b, c, d = reduce_three(b, c, d)

        self.b = b
        self.c = c
        self.d = d
        self.n = n

    def __str__(self):
        return '(%d*sqrt(%d) + %d)/%d' % (self.b, self.n, self.c, self.d)

    def add(self, num):
        return Surd(self.b, self.c + num*self.d, self.d, self.n)

    def recip(self):
        return Surd(self.d*self.b, -self.d*self.c, self.b*self.b*self.n - self.c*self.c, self.n)

    def val(self):
        return (self.b*math.sqrt(self.n) + self.c) / self.d

    def whole(self):
        return int(self.val())


def whole_and_next(a):
    whole = a.whole()
    return whole, a.add(-whole).recip()


def generate_recurring(num):
    a = Surd(1, 0, 1, num)
    for _ in itertools.count():
        whole, a = whole_and_next(a)
        yield whole


def recurring_frac_approximation(recurring):
    f = fractions.Fraction(recurring[-1], 1)
    for i in recurring[-2::-1]:
        f = (1 / f) + i
    return f


def diophantine_solution(x, y, D):
    return (x*x - y*y*D == 1)


def main():
    max_x = 0
    d_for_max_x = None

    for D in range(2, 1000):
        if is_square(D):
            continue

        recurring = []
        for val in generate_recurring(D):
            recurring.append(val)
            approx = recurring_frac_approximation(recurring)
            x = approx.numerator
            y = approx.denominator
            is_dio = diophantine_solution(x, y, D)
            if is_dio:
                if x > max_x:
                    max_x = x
                    d_for_max_x = D
                break
    print(d_for_max_x)


if __name__ == '__main__':
    main()
