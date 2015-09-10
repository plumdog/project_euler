#!/usr/bin/env python3

from sys import argv
import itertools


def lines(fname):
    with open(fname) as f:
        return f.read().splitlines()


def possible_targets(links, starts):
    return {b for a, b in links if a in starts}


def chains_of_length(links, length):
    if length == 0:
        return set()
    if length == 1:
        link_starts = {a for a, _ in links}
        link_ends = {b for _, b in links}
        return link_starts - link_ends
    prev_chains = chains_of_length(links, length - 1)
    new_chains = set()
    for ch in prev_chains:
        for t in possible_targets(links, ch[-1]):
            new_chains.add(ch + t)
    return new_chains


def obeys_all_links(chain, links):
    for a, b in links:
        first_a = chain.find(a)
        last_b = chain.rfind(b)

        if (first_a == -1) or (last_b == -1):
            return False

        if first_a > last_b:
            return False
    return True


def main():
    links = set()

    for triple in lines(argv[1]):
        links.add((triple[0], triple[1]))
        links.add((triple[1], triple[2]))

    for i in itertools.count(1):
        chains = chains_of_length(links, i)

        for ch in chains:
            if obeys_all_links(ch, links):
                print(ch)
                return


if __name__ == '__main__':
    main()
