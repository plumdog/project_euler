#!/usr/bin/env python3

from functools import lru_cache
from sys import argv


def load_tr(fname):
    with open(fname) as f:
        for l in f:
            yield [int(i) for i in l.strip().split()]


def max_path(tr):
    @lru_cache(maxsize=None)
    def tr_sum(row, col):
        try:
            val = tr[row][col]
        except IndexError:
            return 0
        else:
            return val + max(tr_sum(row + 1, col), tr_sum(row + 1, col + 1))
    return tr_sum(0, 0)


if __name__ == '__main__':
    tr = list(load_tr(argv[1]))
    print(max_path(tr))
