#!/usr/bin/env python3

from itertools import permutations


def sub_string_divisibility(p):
    return (slice_divides(p[1:4], 2) and
            slice_divides(p[2:5], 3) and
            slice_divides(p[3:6], 5) and
            slice_divides(p[4:7], 7) and
            slice_divides(p[5:8], 11) and
            slice_divides(p[6:9], 13) and
            slice_divides(p[7:10], 17))


def slice_divides(slice_, div):
    return three_slice_to_int(slice_) % div == 0


def three_slice_to_int(slice_):
    return slice_[0] * 100 + slice_[1] * 10 + slice_[2]


def main():
    total = 0
    for p in permutations(range(10)):
        if sub_string_divisibility(p):
            total += int(''.join(str(d) for d in p))

    print(total)


if __name__ == '__main__':
    main()
