#!/usr/bin/env python3

from functools import lru_cache
from itertools import count


max_ = 4000000


@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def main():
    sum_ = 0
    for val in count():
        fib_val = fib(val)

        if fib_val > max_:
            break

        if fib_val % 2 == 0:
            sum_ += fib_val

    print(sum_)


if __name__ == '__main__':
    main()
