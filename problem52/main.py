#!/usr/bin/env python3

import itertools


def upto_times(num, upto):
    for i in range(2, upto+1):
        if sorted(str(num * i)) != sorted(str(num)):
            return False
    return True

def main():
    for i in itertools.count(1):
        if upto_times(i, 6):
            print(i)
            return

if __name__ == '__main__':
    main()
