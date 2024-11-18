"""
The Depth-First Search (DFS) algorithm is a fundamental graph traversal technique
used to explore all vertices and edges of a graph systematically. DFS explores as far as possible
along each branch before backtracking, which makes it ideal for identifying connected components,
detecting cycles, and solving various graph-related problems.

It is usually implemented by Recursion. But also can be implemented using stack data structure,
which has some advantages, such as - it is unlimited unlike the recursion stack,
and can be used for some very deep and long levels of recursion without going into stack overflow.

The example below is simple, using Recursion
"""


def dfs(node, graph, visited):
    if visited[node]:
        return

    visited[node] = True
    for child in graph[node]:
        dfs(child, graph, visited)

    print(node, end=' ')


graph = [
    [3, 6],             # Node 0
    [2, 3, 4, 5, 6],    # Node 1
    [1, 4, 5],          # Node 2
    [0, 1, 5],          # Node 3
    [1, 2, 6],          # Node 4
    [1, 2, 3],          # Node 5
    [0, 1, 4],          # Node 6
]


visited = [False] * len(graph)


for node in range(len(graph)):
    dfs(node, graph, visited)
