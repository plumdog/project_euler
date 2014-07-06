#!/usr/bin/env python3

import enchant
import sys
import string
import itertools

def main():
    d = enchant.Dict("en_GB")

    with open(sys.argv[1]) as f:
        contents = f.readlines()[0]
    nums = [int(c) for c in contents.split(',')]

    for pw in itertools.product(string.ascii_lowercase, repeat=3):
        decrypt_nums = decrypt(nums, pw)
        text = nums_to_text(decrypt_nums)
        if(is_english(d, text)):
            print(sum(decrypt(nums, pw)))
            return

    
def decrypt(nums, password):
    pwlen = len(password)
    return (n ^ ord(password[i % pwlen]) for i, n in enumerate(nums))


def nums_to_text(nums):
    return ''.join(chr(n) for n in nums)
    

def is_english(d, text):
    """If more than 75% of the text is recognised as English, then that's
    good enough.
    """
    yes = 0
    no = 0
    for w in text.split():
        if d.check(w):
            yes += 1
        else:
            no += 1

        if yes + no > 10:
            if yes < no:
                return False

    return yes > (3 * no)


if __name__ == '__main__':
    #import cProfile
    #cProfile.run('main()')
    main()
