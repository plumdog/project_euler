#!/usr/bin/env python3

import sys
import string
import itertools


def main():
    with open(sys.argv[1]) as f:
        nums = [int(c) for c in f.readline().split(',')]

    for pw in itertools.product(string.ascii_lowercase, repeat=3):
        decrypted_nums = decrypt(nums, pw)

        """If a string contains the word 'the', then its English. We could use
        a proper dictionary or some knowledge of ngrams, but this
        works.
        """

        if 'the' in ''.join(chr(n) for n in decrypted_nums).split():
            print(sum(decrypted_nums))
            return


def decrypt(nums, password):
    pwlen = len(password)
    return [n ^ ord(password[i % pwlen]) for i, n in enumerate(nums)]


if __name__ == '__main__':
    main()
