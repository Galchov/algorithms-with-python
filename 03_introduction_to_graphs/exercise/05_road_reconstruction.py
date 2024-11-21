"""
The task is to find all critical edges - edges without which a node becomes unreachable / separate component

Input:
    5
    5
    1 - 0
    0 - 2
    2 - 1
    0 - 3
    3 - 4
Output:
    0 3
    3 4
"""


def dfs(node, graph, visited):
    if visited[node]:
        return

    visited[node] = True
    for child in graph[node]:
        dfs(child, graph, visited)


n_buildings = int(input())  # Nodes
n_streets = int(input())    # Edges

graph = [[] for _ in range(n_buildings)]
edges = []

for _ in range(n_streets):
    first, second = [int(x) for x in input().split(" - ")]
    graph[first].append(second)
    graph[second].append(first)
    edges.append((min(first, second), max(first, second)))

print(f"Important streets:")
for first, second in edges:
    graph[first].remove(second)
    graph[second].remove(first)

    visited = [False] * n_buildings

    dfs(0, graph, visited)

    if not all(visited):
        print(first, second)

    graph[first].append(second)
    graph[second].append(first)

