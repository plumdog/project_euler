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
        return Surd(self.b, self.c + num*self.d, self.d, self.n, reduce=False)

    def recip(self):
        return Surd(self.d*self.b, -self.d*self.c,
                    self.b*self.b*self.n - self.c*self.c, self.n)

    def val(self):
        return (self.b*math.sqrt(self.n) + self.c) / self.d

    def whole(self):
        return int(self.val())


def whole_and_next(a):
    whole = a.whole()
    return whole, a.add(-whole).recip()


def check_repeats(l, length, repeats):
    for i in range(1, repeats):
        if l[:length] != l[i*length:(i+1)*length]:
            return False
    return True


def recurring_frac_length(num):
    frac_bits = []
    a = Surd(1, 0, 1, num)
    _, a = whole_and_next(a)
    tols = {10: 10, 20: 3, None: 2}

    for i in itertools.count(1):
        if i < 10:
            required_length = i*tols[10]
        elif i < 20:
            required_length = i*tols[20]
        else:
            required_length = i*tols[None]

        while len(frac_bits) < required_length:
            whole, a = whole_and_next(a)
            frac_bits.append(whole)

        if i < 10:
            if check_repeats(frac_bits, i, tols[10]):
                return i
        elif i < 20:
            if check_repeats(frac_bits, i, tols[20]):
                return i
        else:
            if check_repeats(frac_bits, i, tols[None]):
                return i
    return None


def main():
    MAX = 10000
    nums = [recurring_frac_length(num) for num in range(1, MAX)
            if not is_square(num)]
    odd_nums = [n for n in nums if (n % 2 == 1)]
    print(len(odd_nums))


if __name__ == '__main__':
    main()
