#!/usr/bin/env python3

import sys
sys.path.insert(0, '../../common/python')
import special_set_sum


def main():
    count = 0
    set_ = set(range(12))

    As = []

    for A in special_set_sum.powerset(set_):
        As.append(A)
        for B in special_set_sum.powerset(set_ - A, maxsize=len(A), minsize=len(A)):
            if B in As:
                continue

            lenA = len(A)
            lenB = len(B)

            len_check = (lenA > 1) and (lenB > 1) and (lenA == lenB)
            max_min_check = not ((min(A) > max(B)) or (min(B) > max(A)))
            not_all_lower = not (all(i < j for i, j in zip(sorted(A), sorted(B)))
                             or all(i < j for i, j in zip(sorted(B), sorted(A))))

            if len_check and max_min_check and not_all_lower:
                count += 1
    print(count)


if __name__ == '__main__':
    main()
