"""
Given a directed graph and a start vertex, the output will be all vertices,
that cannot be reached.

Simple solution, using Depth-First Search algorithm.
"""


def dfs(node, graph, visited):
    if node in visited:
        return

    visited.add(node)
    for child in graph[node]:
        dfs(child, graph, visited)


nodes = int(input())
edges = int(input())

graph = {node: [] for node in range(1, nodes + 1)}

for _ in range(edges):
    source, destination = [int(x) for x in input().split()]
    graph[source].append(destination)

start_node = int(input())

visited = set()

dfs(start_node, graph, visited)

unreachable_nodes = [node for node in graph if node not in visited]
print(*unreachable_nodes, sep=' ')
