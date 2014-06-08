#!/usr/bin/env python3

# We only need to check n up to 9, as n = 10 with the smallest value,
# 1, would give: 12345678910 which is too big.

from itertools import count


def concatenated_product(val, with_vals):
    products = []
    for with_val in range(1, with_vals + 1):
        products.append(val * with_val)
    return ''.join(str(p) for p in products)


def pandigital(s):
    return (len(s) == 9) and (set(s) == set('123456789'))


def pandigital_concatenated_product(val, with_vals):
    return pandigital(concatenated_product(val, with_vals))


def main():
    max_ = 0
    for n in range(2, 10):
        # Keep increasing the trial number, and if the concat gets too
        # big, then stop increasing the trial number and move onto the
        # next value for n
        for num in count(1):
            concat = concatenated_product(num, n)
            if len(concat) >= 10:
                break
            if pandigital(concat):
                max_ = max(max_, int(concat))
    print(max_)


if __name__ == '__main__':
    main()
