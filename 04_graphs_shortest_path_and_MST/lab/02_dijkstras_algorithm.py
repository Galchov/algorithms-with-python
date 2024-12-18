from collections import deque
from queue import PriorityQueue


class Edge:
    def __init__(self, source: int, destination: int, weight: int) -> None:
        self.source = source
        self.destination = destination
        self.weight = weight


edges = int(input())
graph = {}

for _ in range(edges):
    source, destination, weight = [int(x) for x in input().split(', ')]

    if source not in graph:
        graph[source] = []
    if destination not in graph:
        graph[destination] = []
    graph[source].append(Edge(source, destination, weight))

start_node = int(input())
destination_node = int(input())

max_node = max(graph.keys())

distance = [float('inf')] * (max_node + 1)
parent = [None] * (max_node + 1)

distance[start_node] = 0

pq = PriorityQueue()
pq.put((0, start_node))

while not pq.empty():
    min_distance, node = pq.get()
    if node == destination_node:
        break
    for edge in graph[node]:
        new_distance = min_distance + edge.weight
        if new_distance < distance[edge.destination]:
            distance[edge.destination] = new_distance
            parent[edge.destination] = node
            pq.put((new_distance, edge.destination))

if distance[destination_node] == float('inf'):
    print("There is no such path.")
else:
    print(distance[destination_node])

    path = deque()
    node = destination_node
    while node is not None:
        path.appendleft(node)
        node = parent[node]
    print(*path, sep=' ')
