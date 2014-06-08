#!/usr/bin/env python3

import functools


def collatz(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3*n + 1

@functools.lru_cache(maxsize=None)
def collatz_chain_length(n):
    if n == 1:
        return 1
    else:
        return 1 + collatz_chain_length(collatz(n))

def chains(upto):
    longest_chain_length = 0
    value = None
    for i in range(1, upto):
        ch_len = collatz_chain_length(i)
        if ch_len > longest_chain_length:
            longest_chain_length = ch_len
            value = i
    return value


if __name__ == '__main__':
    print(chains(1000000))
