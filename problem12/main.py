#!/usr/bin/env python3

import math
import itertools

NUM = 500

def divisors(num):
    if num <= 3:
        return 2
    divs = 2 # 1 and num
    for i in range(2, int(math.ceil(math.sqrt(num)))):
        if num % i == 0:
            divs += 2
    return divs

def triangle(num):
    return num * (num + 1) // 2

def first_tr_with_divisors(num):
    for i in itertools.count():
        tr = triangle(i)
        if divisors(tr) > num:
            return tr

if __name__ == '__main__':
    print(first_tr_with_divisors(NUM))
