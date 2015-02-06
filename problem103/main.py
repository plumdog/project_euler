#!/usr/bin/env python3

import sys
sys.path.insert(0, '../common/python')

import itertools
import copy
import special_set_sum


def every_ordering(iterable, len_):
    if len_ == 0:
        yield []
    else:
        for sub in every_ordering(iterable, len_ - 1):
            yield from (sub + [v] for v in iterable)


def main():
    delta_range = list(range(-4, 0))
    start = [22,33,39,42,44,45,46]
    LEN = 7
    min_sum_set = start
    min_sum = sum(min_sum_set)
    d = None

    for v in every_ordering(delta_range, LEN):
        trial = {a + delta for a, delta in zip(start, v)}
        if len(trial) == LEN:
            if special_set_sum.is_special_set_sum(trial):
                if sum(trial) < min_sum:
                    min_sum_set = trial
                    min_sum = sum(min_sum_set)
    print(''.join(str(s) for s in sorted(min_sum_set)))


if __name__ == '__main__':
    main()
