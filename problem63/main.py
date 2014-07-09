#!/usr/bin/env python3

import itertools

"""It turns out, 21 is the last value for i. Not sure if I have any
logic to back that up though.
"""

def main():
    count = 0
    for i in range(22):
        for e in range(1, 10):
            if len(str(e**i)) == i:
                count += 1
    print(count)

if __name__ == '__main__':
    main()
