"""
Using Kruskal's Algorithm for Minimum Spanning Tree
"""


class Edge:
    def __init__(self, source: int, destination: int, weight: int):
        self.source = source
        self.destination = destination
        self.weight = weight


def find_root(parent, node):
    # Find parent of node by index in the parent list, until reaching the tree's root
    while node != parent[node]:
        node = parent[node]
    return node


nodes = int(input())    # Towns
edges = int(input())    # Roads

graph = []

for _ in range(edges):
    source, destination, weight = [int(x) for x in input().split(' - ')]
    edge = Edge(source, destination, weight)
    graph.append(edge)

# Edges have to be sorted by their weight in increasing order
graph = sorted(graph, key=lambda x: x.weight)
parent = [n for n in range(nodes)]
total_cost = 0

for edge in graph:
    s = edge.source
    d = edge.destination
    w = edge.weight

    source_root = find_root(parent, s)
    destination_root = find_root(parent, d)

    # If both vertices' root is the same, they are part of the same tree
    if source_root == destination_root:
        continue

    # Otherwise, we add the source to the tree
    parent[source_root] = destination_root

    # Here, the value of the newly added edge is added to the min value of the MST
    total_cost += w

    # Optional: See which edges take part of the discovered MST
    # print(s, d, w)

print(f"Total cost: {total_cost}")
