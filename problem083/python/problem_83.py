#!/usr/bin/env python3

import sys
sys.path.insert(0, '../../common/python/')

import functools
import collections
from graph import WeightedGraph


matrix = None


def main():
    global matrix

    with open(sys.argv[1]) as f:
        lines = f.readlines()
    matrix = [[int(n) for n in l.strip().split(',')] for l in lines]

    """
    matrix = [[131, 673, 234, 103, 18],
              [201, 96, 342, 965, 150],
              [630, 803, 746, 422, 111],
              [537, 699, 497, 121, 956],
              [805, 732, 524, 37, 331]]
    """

    matrix_size = len(matrix)
    # the cost of arriving at each node is the value at that node
    g = WeightedGraph()
    for lnum, line in enumerate(matrix):
        for cnum, value in enumerate(line):
            g.add_node((lnum, cnum))
            # from below
            if (0 <= lnum+1 < matrix_size):
                g.add_arc((lnum+1, cnum), (lnum, cnum), value)

            # from above
            if (0 <= lnum-1 < matrix_size):
                g.add_arc((lnum-1, cnum), (lnum, cnum), value)

            # from right
            if (0 <= cnum+1 < matrix_size):
                g.add_arc((lnum, cnum+1), (lnum, cnum), value)

            # from left
            if (0 <= cnum-1 < matrix_size):
                g.add_arc((lnum, cnum-1), (lnum, cnum), value)

    route, cost = a_star(g, (0, 0), (matrix_size-1, matrix_size-1))
    print(cost + matrix[0][0])


def a_star(graph, start, goal, heuristic=None):
    if heuristic is None:
        def heuristic(a, b):
            return 0

    def reconstruct_path(came_from, current_node):
        if current_node in came_from:
            p, cost = reconstruct_path(came_from, came_from[current_node])
            return p + [current_node], cost + graph.arcs[(p[-1], current_node)]
        else:
            return [current_node], 0

    closed_set = set()
    openset = set([start])
    came_from = dict()
    g_score = dict()
    f_score = dict()

    g_score[start] = 0
    f_score[start] = g_score[start] + heuristic(start, goal)

    while openset:
        open_fscores = {node: score for node, score in
                        f_score.items() if node in openset}
        current = min(open_fscores, key=open_fscores.get)
        if current == goal:
            return reconstruct_path(came_from, goal)
        openset.remove(current)
        closed_set.add(current)

        for neighbour, weight in graph.neighbours(current).items():
            if neighbour in closed_set:
                continue
            tentative_g_score = g_score[current] + weight

            if neighbour not in openset or \
               tentative_g_score < g_score[neighbour]:
                came_from[neighbour] = current
                g_score[neighbour] = tentative_g_score
                f_score[neighbour] = (g_score[neighbour] +
                                      heuristic(neighbour, goal))
                if neighbour not in openset:
                    openset.add(neighbour)
    return None


if __name__ == '__main__':
    main()
