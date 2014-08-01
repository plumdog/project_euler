#!/usr/bin/env python3

import sys
sys.path.insert(0, '../common/python/')

from primality import prime_factors

"""
phi(n) = n*sum_{p|n} (1 - 1/p)
1/phi(n) = (1/n)*sum_{p|n} p/(p - 1)
n/phi(n) = sum_{p|n} p/(p - 1)
"""

def n_over_phi(n):
    top = 1
    bot = 1

    pfactors = prime_factors(n)

    for p, count in pfactors.items():
        top *= p
        bot *= (p - 1)
    return top / bot


def maximise_n_over_phi(upto):
    max_value = 0
    max_n = 0

    for n in range(2, upto+1):
        n_over_phi_ = n_over_phi(n)
        if n_over_phi_ > max_value:
            max_value = n_over_phi_
            max_n = n
    return max_n
            
        

def main():
    print(maximise_n_over_phi(1000000))


if __name__ == '__main__':
    main()
