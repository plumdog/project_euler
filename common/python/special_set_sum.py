import itertools


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
