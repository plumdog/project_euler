#!/usr/bin/env python3

import sys


def main():
    fname = sys.argv[1]
    base_exps = {}
    with open(fname) as f:
        for i, l in enumerate(f.readlines()):
            linenum = i + 1
            base, exp = l.strip().split(',')
            base_exps[linenum] = (int(base), int(exp))

    max_ = 0
    max_line = None

    for linenum, (b, e) in base_exps.items():
        small_e = e / 100000
        approx = pow(b, small_e)
        if approx > max_:
            max_ = approx
            max_line = linenum
    print(max_line)
        

if __name__ == '__main__':
    main()
