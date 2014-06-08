#!/usr/bin/env python3

from itertools import permutations

# always:
# [1digit] * [4digit] = [4digit]
# or
# [2digit] * [3digit] = [4digit]
DIGITS = 10

def main():
    unusuals = set()
    # ldigits is used to create the pair to multiply together
    # rdigits is the pair that should be compared to the answer
    for ldigits in permutations(range(1, DIGITS), 5):
        rdigits = tuple(set(range(1, DIGITS)) - set(ldigits))
        for pr in unusual_products(ldigits, rdigits):
            unusuals.add(pr)
    print(sum(unusuals))


def unusual_products(ldigits, rdigits):
    for i in (1, 2):
        a = digits_to_int(ldigits[:i])
        b = digits_to_int(ldigits[i:])
        c = digits_to_int(rdigits)

        c_res = a * b
        if sorted(str(c_res)) == sorted(str(c)):
            yield c_res


def digits_to_int(digits):
    return int(''.join(str(i) for i in digits))
        

if __name__ == '__main__':
    main()
