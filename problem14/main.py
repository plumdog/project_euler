#!/usr/bin/env python3

import functools

@functools.lru_cache(maxsize=None)
def collatz(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3*n + 1

def collatz_chain(n):
    if n == 1:
        return []
    else:
        return [n] + collatz_chain(collatz(n))

def chains(upto):
    longest_chain_length = 0
    value = None
    for i in range(1, upto):
        print(i)
        ch_len = len(collatz_chain(i))
        if ch_len > longest_chain_length:
            longest_chain_length = ch_len
            value = i
    return value

print(chains(1000000))
