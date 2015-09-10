#!/usr/bin/env python3

import sys
sys.path.insert(0, '../../common/python/')

from primality import prime_sieve


def main():
    max_prime = 10000
    max_ = 10000000
    threshold = 0.4

    best_ratio = float("inf")
    best_val = None
    best_phi = None

    # we assume that we should be looking for two primes. We also
    # assume that they should be close together.

    primes = prime_sieve(max_prime)
    for p1 in primes:
        for p2 in primes:
            if p1 * (1.0 - threshold) <= p2 <= p1 * (1.0 + threshold):
                prod = p1 * p2
                if prod > max_:
                    break

                phi = (p1 - 1) * (p2 - 1)
                ratio = prod / phi
                if (sorted(str(phi)) == sorted(str(prod))) and \
                   (ratio < best_ratio):
                    best_phi = phi
                    best_val = prod
                    best_ratio = ratio
            if p2 > p1 * (1.0 + threshold):
                break

    print(best_val)


if __name__ == '__main__':
    main()
