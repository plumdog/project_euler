import collections


class WeightedGraph(object):
    def __init__(self):
        self.nodes = set()
        self.arcs = dict()

    def add_node(self, identifier):
        self.nodes.add(identifier)

    def add_arc(self, source, target, weight=1):
        self.arcs[(source, target)] = weight

    def neighbours(self, node):
        neighbours = {}
        for (source, target), weight in self.arcs.items():
            if source == node:
                neighbours[target] = weight
        return neighbours

    def __repr__(self):
        neighbours = collections.defaultdict(list)
        for (source, target), weight in self.arcs.items():
            neighbours[source].append((target, weight))

        out = []
        for source, targets_and_weights in sorted(neighbours.items()):
            out.append(str(source) + ':\t' + str(targets_and_weights))
        return '\n'.join(out)
