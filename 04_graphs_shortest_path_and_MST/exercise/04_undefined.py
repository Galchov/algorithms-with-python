"""
Using Bellman Ford's Algorithm
"""


from collections import deque


def find_path(parent, node):
    result = deque()
    while node is not None:
        result.appendleft(node)
        node = parent[node]
    return result


nodes = int(input())
edges = int(input())

graph = []

for _ in range(edges):
    source, destination, weight = [int(x) for x in input().split()]
    graph.append((source, destination, weight))

start_node = int(input())
end_node = int(input())

distance = [float('inf')] * (nodes + 1)
distance[start_node] = 0
parent = [None] * (nodes + 1)

for _ in range(nodes - 1):
    for source, destination, weight in graph:
        if distance[source] == float('inf'):
            continue

        new_distance = distance[source] + weight
        if new_distance < distance[destination]:
            distance[destination] = new_distance
            parent[destination] = source

for source, destination, weight in graph:
    new_distance = distance[source] + weight
    if new_distance < distance[destination]:
        print('Undefined')
        break
else:
    path = find_path(parent, end_node)
    print(*path, sep=' ')
    print(distance[end_node])
