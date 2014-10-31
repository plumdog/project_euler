#!/usr/bin/env python3

import math
import fractions
import collections


def main():
    max_ = 1500000

    # we only need to go to this limit as one our sides is generated
    # as m^2+n^2
    limit = int(math.sqrt(max_ // 2))

    count = collections.defaultdict(int)
    for m in range(2, limit):
        for n in range(1, m):
            if ((m + n) % 2 == 1) and (fractions.gcd(m, n) == 1):
                a = m*m + n*n
                b = m*m - n*n
                c = 2*m*n
                length = a + b + c

                trial_length = length
                while trial_length < max_:
                    count[trial_length] += 1
                    trial_length += length
    singles = [length for (length, lcount) in count.items() if lcount == 1]
    print(len(list(singles)))


if __name__ == '__main__':
    main()
