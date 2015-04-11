#!/usr/bin/env python3


import sys
import itertools
import functools
import collections


def numbers(upto, extras=(), *, mult=1):
    letter = {1: 'S', 2: 'D', 3: 'T'}[mult]
    return {n * mult: '{}{}'.format(letter, n) for n in itertools.chain(range(1, upto+1), extras)}

SINGLES = numbers(20, [25])
DOUBLES = numbers(20, [25], mult=2)
TREBLES = numbers(20, mult=3)


ALL = list(SINGLES.items()) + list(DOUBLES.items()) + list(TREBLES.items())


Checkout = collections.namedtuple('Checkout', ['first', 'second', 'final', 'total'])

def checkouts():

    def _make_checkout(first, second, final):
        darts = (first, second, final)
        return Checkout(first, second, final,
                        sum(d[0] for d in darts if d))

    checkouts_ = []

    for final in DOUBLES.items():
        for second in ALL:
            # Slightly sneaky here. a and second are tuples of (score,
            # string_representation), and by comparing, we ensure that
            # first <= second, and so we never get checkouts like (a,
            # b, c) and (b, a, c) in our output, which we want to
            # exclude.
            for first in (a for a in ALL if a <= second):
                checkouts_.append(_make_checkout(first, second, final))
            # Also add a checkout with just two darts
            checkouts_.append(_make_checkout(None, second, final))
        # Also add a checkout with just one dart
        checkouts_.append(_make_checkout(None, None, final))
    return checkouts_


def main():
    print(sum(1 for c in checkouts() if c.total < 100))


if __name__ == '__main__':
    main()
