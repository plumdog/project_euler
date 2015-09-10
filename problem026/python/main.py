#!/usr/bin/env python3

"""This checks to see if a fraction, 1/d can be written:
1/d x 10^i - 1/d in N
which is done by checking if there is an i such that:
10^i - 1 = 0 mod d

However, this only checks fractions that have decimal representations
that have no prefix, ie it does check 1/3 = 0.333... but not
1/6 = 0.1666...

This is good enough because a) it gives the right answer, and b) I
think because for any 1/d that has a prefix and recursion length a,
there is a value c < d without a recursion with recursion >= a. I have
work to do to fully convince myself, but maybe I'll sure this bit of
logic up one day.

"""


max_ = 1000
max_power = 1000


def main():
    max_length = 0
    val_with_max_length = None

    for val in range(2, max_):
        l = frac_recursion_length(val)
        if l and l > max_length:
            max_length = l
            val_with_max_length = val

    print(val_with_max_length)


def frac_recursion_length(val):
    for i in range(1, max_power):
        if (10**i - 1) % val == 0:
            return i


if __name__ == '__main__':
    main()
