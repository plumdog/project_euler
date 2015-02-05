#!/usr/bin/env python3


import itertools
import copy


def powerset(set_, include_empty_set=False, maxsize=None, minsize=None):
    if maxsize is None:
        maxsize = len(set_) + 1
    if minsize is None:
        if include_empty_set:
            minsize = 0
        else:
            minsize = 1
    for n in range(minsize, maxsize + 1):
        yield from (set(c) for c in itertools.combinations(set_, n))


def is_special_set_sum(set_):
    for A in powerset(set_):
        sum_a = sum(A)
        for B in powerset(set_ - A):
            sum_b = sum(B)
            if (sum_a == sum_b) or ((len(A) > len(B)) and (sum_a < sum_b)):
                return False
    return True


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
            if is_special_set_sum(trial):
                if sum(trial) < min_sum:
                    min_sum_set = trial
                    min_sum = sum(min_sum_set)
    print(''.join(str(s) for s in sorted(min_sum_set)))


if __name__ == '__main__':
    main()
