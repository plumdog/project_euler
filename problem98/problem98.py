#!/usr/bin/env python3

import math
import sys
import collections
import itertools


def is_square(num):
    sqrt = math.sqrt(num)
    return int(sqrt)**2 == num


def word_to_value(word, mapping):
    return int(''.join(str(mapping[ch]) for ch in word))


def find_square_anagram(word1, word2):
    assert sorted(word1) == sorted(word2)
    letters = list(set(word1))
    numbers = list(range(1, 10))

    mappings = (dict(zip(letters, kperm))
                for kperm in itertools.permutations(numbers, len(letters)))

    for mapping in mappings:
        v1 = word_to_value(word1, mapping)
        v2 = word_to_value(word2, mapping)
        if is_square(v1) and is_square(v2):
            yield (v1, v2)


def main():
    fname = sys.argv[1]
    with open(fname) as f:
        l = f.readline()
        words = [word.strip('"') for word in l.split(',')]

    find_anagrams = {word: sorted(word) for word in words}
    anagrams = collections.defaultdict(list)
    for k, v in find_anagrams.items():
        anagrams[''.join(v)].append(k)
    anagrams = {k: v for k, v in anagrams.items() if len(v) > 1}

    max_ = 0

    for words in anagrams.values():
        for (w1, w2) in itertools.combinations(words, 2):
            for sq1, sq2 in find_square_anagram(w1, w2):
                max_ = max(max_, sq1, sq2)
    print(max_)


if __name__ == '__main__':
    main()
