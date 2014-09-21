#!/usr/bin/env python3

import sys
sys.path.insert(0, '../common/python/')

import primality


def main():
    max_ = 1000000
    max_ = 1000

    max_ = int(sys.argv[1])

    total = 0

    for d in range(2, max_+1):
        total += primality.phi(d)
    print(total)
                
        


if __name__ == '__main__':
    main()
