"""
The task is to make the graph acyclic by removing minimal number of edges.
If several edges can be removed to break a cycle, start from the smallest one in alphabetical order.

Input:
    8
    1 -> 2 5 4
    2 -> 1 3
    3 -> 2 5
    4 -> 1
    5 -> 1 3
    6 -> 7 8
    7 -> 6 8
    8 -> 6 7
Output:
    Edges to remove: 2
    1 - 2
    6 - 7
"""


def dfs(node, destination, graph, visited):
    if node in visited:
        return

    visited.add(node)

    if node == destination:
        return
    for child in graph[node]:
        dfs(child, destination, graph, visited)


def path_exists(source, destination, graph):
    visited = set()

    dfs(source, destination, graph, visited)

    return destination in visited


nodes = int(input())

graph = {}
edges = []
for _ in range(nodes):
    node, children_str = input().split(" -> ")
    children = children_str.split()
    graph[node] = children
    for child in children:
        edges.append((node, child))

removed_edges = []
for source, destination in sorted(edges, key=lambda x: (x[0], x[1])):
    if destination not in graph[source] or source not in graph[destination]:
        continue

    graph[source].remove(destination)
    graph[destination].remove(source)

    if path_exists(source, destination, graph):
        removed_edges.append((source, destination))
    else:
        graph[source].append(destination)
        graph[destination].append(source)

print(f"Edges to remove: {len(removed_edges)}")
for source, destination in removed_edges:
    print(f"{source} - {destination}")
