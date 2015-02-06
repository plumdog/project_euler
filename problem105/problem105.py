#!/usr/bin/env python3

import sys
sys.path.insert(0, '../common/python')
import special_set_sum


def main():
    with open(sys.argv[1]) as f:
        lines = f.read().splitlines()
    sets = (set(int(num) for num in l.split(',')) for l in lines)
    total = sum(sum(s) for s in sets if special_set_sum.is_special_set_sum(s))
    print(total)


if __name__ == '__main__':
    main()
