#!/usr/bin/env python3

import sys
sys.path.insert(0, '../../common/python/')
import copy
import collections

from graph import WeightedGraph





def main():
    with open(sys.argv[1]) as f:
        lines = f.read().splitlines()

    adj = []
    for line in lines:
        row = []
        for node in line.split(','):
            if node == '-':
                row.append(None)
            else:
                row.append(int(node))
        adj.append(row)

    num_nodes = len(adj)
    # make sure the adjacency matrix is square
    assert all(len(row) == num_nodes for row in adj)

    graph = WeightedGraph()
    for i in range(num_nodes):
        graph.add_node(i)

    for x, row in enumerate(adj):
        for y, weight in enumerate(row):
            if weight is not None:
                graph.add_arc(x, y, weight)

    mst = min_spanning_tree(graph)

    # Now we want to consider half of the adjacency matrix, so we can
    # sum the total weight of all arcs.

    half_adj = []
    for i, row in enumerate(adj):
        new_row = []
        for j, weight in enumerate(row):
            if i <= j:
                new_row.append(weight)
            else:
                new_row.append(None)
        half_adj.append(new_row)

    # Now remove all of the arcs in the mst, so the arcs we are left
    # with are the ones that we are able to remove.
    for mst_arc_source, mst_arc_target in mst:
        half_adj[mst_arc_source][mst_arc_target] = None
        half_adj[mst_arc_target][mst_arc_source] = None
    print(sum(sum(filter(None, row)) for row in half_adj))


def min_spanning_tree(graph):
    available_nodes = copy.copy(graph.nodes)

    chosen_nodes = set()
    chosen_arcs = set()

    # Initial node
    chosen_node = available_nodes.pop()
    chosen_nodes.add(chosen_node)

    while(available_nodes):
        # Build a dict of target: (source, weight), where weight is
        # the minimum of all arcs from chosen_nodes to target.
        neighbours_and_weights = {}
        for chosen_node in chosen_nodes:
            for neighbour, weight in graph.neighbours(chosen_node).items():
                if neighbour in available_nodes:
                    if neighbour in neighbours_and_weights:
                        current_weight = neighbours_and_weights[neighbour][1]
                        if weight < current_weight:
                            neighbours_and_weights[neighbour] = (chosen_node, weight)
                    else:
                        neighbours_and_weights[neighbour] = (chosen_node, weight)

        shortest_weight = float('inf')
        shortest_target = None
        shortest_source = None
        for target, (source, weight) in neighbours_and_weights.items():
            if weight < shortest_weight:
                shortest_weight = weight
                shortest_target = target
                shortest_source = source

        old_len = len(chosen_arcs)
        chosen_arcs.add((shortest_source, shortest_target))

        available_nodes.remove(shortest_target)
        chosen_nodes.add(shortest_target)
        
    return chosen_arcs

        
            
        


if __name__ == '__main__':
    main()
