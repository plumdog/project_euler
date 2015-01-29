#!/usr/bin/env python3

import sys
sys.path.insert(0, '../common/python/')

from primality import prime_sieve


def max_len_prime(max_):
    primes = list(sorted(prime_sieve(max_)))

    num_primes = len(primes)
    max_len = 1
    max_len_prime = None
    for length in range(21, 10000):
        trial = None
        for start in range(num_primes - length):
            # if we have an even number of terms and 2 is not
            # included, then skip
            if (start != 0) and (length % 2 == 0):
                break

            trial = sum(primes[start:start+length])

            if trial >= max_:
                # if the max has been reached, but we're still at the
                # start, then all done.
                if start == 0:
                    return max_len_prime
                else:
                    break
            elif (trial in primes) and (length > max_len):
                max_len = length
                max_len_prime = trial
                break


def main():
    max_ = 1000000
    print(max_len_prime(max_))


if __name__ == '__main__':
    main()
