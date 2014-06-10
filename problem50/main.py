#!/usr/bin/env python3

import sys
sys.path.insert(0, '../common/python/')

from primality import prime_sieve


def int_permutations(num):
    for perm in permutations(str(num)):
        out = int(''.join(perm))
        if out > num:
            yield out

def main():
    max_ = 1000000
    primes = list(sorted(prime_sieve(max_)))
    max_len = 536
    max_trial_len = 4000
    max_len_prime = None
    for length in range(max_len, 538):
        for start in range(max_):
            trial = sum(primes[start:start+length])
            if trial in primes and (length > max_len):
                max_len = length
                max_len_prime = trial
                print(max_len_prime)
                #return
            elif trial > max_:
                continue
    
                

if __name__ == '__main__':
    main()
