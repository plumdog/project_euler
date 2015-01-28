#!/usr/bin/env python3
"""
total, T = B + R

P(BB) = (B/T)*(B-1/T-1)
P(BB) = 1/2
  => 1/2 = (B/T)*(B-1/T-1)
1 = 2*(B/T)*(B-1/T-1)
T*(T-1) = 2*B*(B-1)
        = 2*B^2 - 2B
T^2 - T = 2*B^2 - 2B
T^2 - T - 2B^2 + 2B = 0

then for reasons:

B_{k+1} = 3*B_k + 2*T_k - 2
n_{k+1} = 4*B_k + 3*T_k - 3

"""

import itertools


MAX = 1000000000000

def main():
    b, n = 15, 21
    while n <= MAX:
        b, n = 3*b + 2*n - 2, 4*b + 3*n - 3
    print(b)
        

if __name__ == '__main__':
    main()
