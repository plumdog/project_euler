#!/usr/bin/env python3

import collections


def main():
    count = collections.defaultdict(int)
    count[0] = 1

    for first_num in range(1, 100):
        for total in range(first_num, 101):
            count[total] += count[total - first_num]
    print(count[100])


if __name__ == '__main__':
    main()
