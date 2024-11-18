"""
You are given an undirected graph with nodes/vertices numbered from 0 to n-1,
and not all nodes/vertices are necessarily connected. The goal is to find all
separate connected components within this graph and list the nodes/vertices in each component.

Input:
    Number of nodes -> 9

    For each node, there are the following neighbours:
    Node 0 -> 3 6
    Node 1 -> 3 4 5 6
    Node 2 -> 8
    Node 3 -> 0 1 5
    Node 4 -> 1 6
    Node 5 -> 1 3
    Node 6 -> 0 1 4
    Node 7 -> No neighbours
    Node 8 -> 2
"""


def generate_graph(nodes):
    graph = {}

    for node_value in range(nodes):
        edges = [int(x) for x in input().split()]
        if node_value not in graph:
            graph[node_value] = edges

    return graph


def find_connected_components(nodes, graph):
    visited = set()
    connected_components = []

    def dfs(node, graph, visited, component):
        visited.add(node)
        component.append(node)

        for neighbour in graph[node]:
            if neighbour not in visited:
                dfs(neighbour, graph, visited, component)

    for node in range(nodes):
        if node not in visited:
            component = []
            dfs(node, graph, visited, component)
            connected_components.append(component)

    return connected_components


nodes = int(input())
graph = generate_graph(nodes)
result = find_connected_components(nodes, graph)
for comp in result:
    print(f"Connected component: {' '.join(str(c) for c in comp)}")
