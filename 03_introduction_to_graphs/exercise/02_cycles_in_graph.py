"""
Find whether a graph is Acyclic.

Input:
    A-F
    F-D
    D-A
    End
Output:
    Acyclic: No
"""


def dfs(node, graph, visited, cycles):
    if node in cycles:
        raise Exception

    if node in visited:
        return

    visited.add(node)
    cycles.add(node)

    for child in graph[node]:
        dfs(child, graph, visited, cycles)

    cycles.remove(node)


graph = {}

while True:
    line = input()

    if line == "End":
        break

    source, destination = line.split('-')
    if source not in graph:
        graph[source] = []
    if destination not in graph:
        graph[destination] = []

    graph[source] = destination

try:
    visited = set()
    for node in graph:
        if node not in visited:
            dfs(node, graph, visited, set())
    print("Acyclic: Yes")
except Exception:
    print("Acyclic: No")
