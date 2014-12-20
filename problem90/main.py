#!/usr/bin/env python3

import itertools

def main():
    nums = list(range(10))
    choices = 6

    cube_pairs = set()

    for cube1 in (frozenset(c) for c in itertools.combinations(nums, choices)):
        for cube2 in (frozenset(c) for c in itertools.combinations(nums, choices)):
            if all_squares(cube1, cube2):
                cube_pairs.add(frozenset([cube1, cube2]))

    print(len(cube_pairs))

    


def all_squares(cube1, cube2):
    return (can_show(cube1, cube2, 0, 1) and 
            can_show(cube1, cube2, 0, 4) and 
            can_show(cube1, cube2, 0, 9) and
            can_show(cube1, cube2, 1, 6) and 
            can_show(cube1, cube2, 2, 5) and
            can_show(cube1, cube2, 3, 6) and
            can_show(cube1, cube2, 4, 9) and
            can_show(cube1, cube2, 6, 4) and
            can_show(cube1, cube2, 8, 1))
        


def can_show(cube1, cube2, digit1, digit2):
    return ((cube_can_show(cube1, digit1) and
             cube_can_show(cube2, digit2)) or
            (cube_can_show(cube1, digit2) and
             cube_can_show(cube2, digit1)))


def cube_can_show(cube, digit):
    if (digit == 6) or (digit == 9):
        return (6 in cube) or (9 in cube)
    return (digit in cube)
    

if __name__ == '__main__':
    main()
