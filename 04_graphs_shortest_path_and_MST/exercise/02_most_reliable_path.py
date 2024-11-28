"""
Used Dijkstra's Algorithm - Slightly modified
"""


from collections import deque
from queue import PriorityQueue


class Edge:
    def __init__(self, first: int, second: int, weight: int) -> None:
        self.first = first
        self.second = second
        self.weight = weight


nodes = int(input())
edges = int(input())

graph = []  # [Node 0 -> [Edge(s, d, w) -> for each child], Node 1 -> [Edge(s, d, w) ...], ...]
[graph.append([]) for _ in range(nodes)]

for _ in range(edges):
    # first -> int; second -> int; weight -> int in %
    first, second, weight = [int(x) for x in input().split()]
    edge = Edge(first, second, weight)
    graph[first].append(edge)
    graph[second].append(edge)

start_node = int(input())
end_node = int(input())

# Keeps track of the current shortest (most reliable) path
pq = PriorityQueue()
pq.put((-100, start_node))

distance = [float('-inf')] * nodes
distance[start_node] = 100
parent = [None] * nodes

while not pq.empty():
    current_distance, current_node = pq.get()
    if current_node == end_node:
        break
    for edge in graph[current_node]:
        # For debugging:
        s = edge.first
        d = edge.second
        w = edge.weight

        new_distance = -current_distance * edge.weight / 100
        child = edge.second if edge.first == current_node else edge.first
        if new_distance > distance[child]:
            distance[child] = new_distance
            parent[child] = current_node
            pq.put((-new_distance, child))


path = deque()
node = end_node

while node is not None:
    path.appendleft(node)
    node = parent[node]

print(f"Most reliable path reliability: {distance[end_node]:.2f}%")
print(*path, sep=' -> ')
