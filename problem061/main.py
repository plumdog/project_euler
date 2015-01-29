#!/usr/bin/env python3

import itertools


def p3(n):
    return n * (n+1) // 2


def p4(n):
    return n*n


def p5(n):
    return n*(3*n-1) // 2


def p6(n):
    return n*(2*n-1)


def p7(n):
    return n*(5*n-3) // 2


def p8(n):
    return n*(3*n-2)


def all_four_digits(f):
    """For the given method, gets all four digit numbers. The function is
    assumed to be monotonically increasing, that is, once a result has
    5 digits, there are asumed to be no more.
    """
    out = set()
    for i in itertools.count():
        val = f(i)
        if 1000 <= val < 10000:
            out.add(val)
        elif val >= 10000:
            break
    return out


def is_one_of_each(fours, tup):
    count = {v: set() for v in tup}
    for v, (k, vs) in itertools.product(tup, fours.items()):
        if v in vs:
            count[v].add(k)
    return any(sorted(order) == [3, 4, 5, 6, 7, 8] for order
               in itertools.product(*count.values()))


def arc(v1, v2):
    return (v1 // 100) == (v2 % 100)


def main():
    fs = {3: p3,
          4: p4,
          5: p5,
          6: p6,
          7: p7,
          8: p8}

    fours = {i: all_four_digits(f) for i, f in fs.items()}
    all_ = set.union(*fours.values())

    adj = {}
    for k, vs in fours.items():
        adj.update({v: {n for n in all_ if arc(n, v)} for v in vs})

    g = Graph(adj)
    cycles = g.find_cycles_of_length(6)

    for c in cycles:
        if is_one_of_each(fours, c):
            print(sum(c))
            return


class Graph(object):
    def __init__(self, adj):
        self.adj = adj

    def find_all_paths(self, start, end, path=[], *, max_length=None):
        path = path + [start]

        if max_length and (len(path) > max_length+1):
            return []

        if start == end:
            return [path]
        if start not in self.adj:
            return []
        paths = []
        for node in self.adj[start]:
            if node not in path:
                paths.extend(
                    self.find_all_paths(
                        node, end, path, max_length=max_length))
        return paths

    def find_cycles_of_length(self, n):
        if n < 3:
            return []
        cycles = set()
        for start, neighbours in self.adj.items():
            for neighbour in neighbours:
                for path in self.find_all_paths(
                        neighbour, start, max_length=n-1):
                    if len(path) == n:
                        cycles.add(tuple(sorted(path)))
        return cycles


if __name__ == '__main__':
    main()
