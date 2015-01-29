#!/usr/bin/env python3

import sys
import functools


matrix = None


def main():
    global matrix

    with open(sys.argv[1]) as f:
        lines = f.readlines()
    matrix = [[int(n) for n in l.strip().split(',')] for l in lines]

    """
    matrix = [[131, 673, 234, 103, 18],
              [201, 96, 342, 965, 150],
              [630, 803, 746, 422, 111],
              [537, 699, 497, 121, 956],
              [805, 732, 524, 37, 331]]
    """

    shortest = float('inf')
    for start in range(len(matrix)):
        shortest = min(shortest_path(0, start), shortest)
    print(shortest)


@functools.lru_cache(maxsize=None)
def shortest_path(x, y, last=None):
    """last = +1 indicates that the last move was up, -1 indicates the
    last move was down, any other value is ignored
    """
    global matrix
    try:
        value = matrix[y][x]
    except IndexError:
        return float('inf')

    right = shortest_path(x+1, y)

    if right == float('inf'):
        # then we've reached the right hand side. Just return the
        # value here
        return value

    down = None
    up = None
    if last == -1:
        # our last move was down, so we effectively ban a move up
        # again to remove the infinite loop
        up = float('inf')
    elif last == +1:
        down = float('inf')

    if down is None:
        down = shortest_path(x, y+1, -1)

    if up is None:
        up = shortest_path(x, y-1, +1)

    return value + min(up, right, down)

if __name__ == '__main__':
    main()
