#!/usr/bin/env python3

import sys
sys.path.insert(0, '../../common/python/')

import primality
import functools


def main():
    max_ = 8500
    primes = primality.prime_sieve(max_)

    for ai, a in primes_from(primes):
            for bi, b in primes_from(primes, ai+1):
                if meets_condition(a, b):
                    for ci, c in primes_from(primes, bi+1):
                        if meets_condition(a, c) and meets_condition(b, c):
                            for di, d in primes_from(primes, ci+1):
                                if meets_condition(a, d) and \
                                   meets_condition(b, d) and \
                                   meets_condition(c, d):
                                    for ei, e in primes_from(primes, di+1):
                                        if meets_condition(a, e) and \
                                           meets_condition(b, e) and \
                                           meets_condition(c, e) and \
                                           meets_condition(d, e):

                                            print(a + b + c + d + e)
                                            return


def primes_from(primes, from_=0):
    return ((ai, a) for (ai, a) in enumerate(primes) if ai >= from_)


@functools.lru_cache(maxsize=None)
def meets_condition(a, b):
    return primality.is_prime(int(str(a) + str(b))) and \
        primality.is_prime(int(str(b) + str(a)))


if __name__ == '__main__':
    main()
