#!/usr/bin/env python3

from functools import lru_cache
from itertools import count


@lru_cache(maxsize=None)
def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def main():
    strlen = 1000

    for val in count(1):
        if len(str(fib(val))) >= strlen:
            break

    print(val)


if __name__ == '__main__':
    main()
