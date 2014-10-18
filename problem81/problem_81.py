#!/usr/bin/env python3

import sys
import functools

matrix = None

def main():
    global matrix

    with open(sys.argv[1]) as f:
        lines = f.readlines()
    matrix = [[int(n) for n in l.strip().split(',')] for l in lines]

    print(shortest_path(0, 0))


@functools.lru_cache(maxsize=None)
def shortest_path(x, y):
    global matrix
    try:
        value = matrix[x][y]
    except IndexError:
        return float('inf')

    right = shortest_path(x+1, y)
    down = shortest_path(x, y+1)

    
    if (right == float('inf')) and (down == float('inf')):
        # then we're in the bottom right. Just return the value here
        return value
    else:
        # otherwise, return the value here plus the lesser of the two
        # paths
        return value + min(right, down)

if __name__ == '__main__':
    main()
