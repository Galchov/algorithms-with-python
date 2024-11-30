"""
Used Prim's Algorithm
"""


from queue import PriorityQueue


class Edge:
    def __init__(self, first: int, second: int, weight: int) -> None:
        self.first = first
        self.second = second
        self.weight = weight

    def __gt__(self, other) -> bool:
        return self.weight > other.weight


budget = int(input())
nodes = int(input())
edges = int(input())

graph = [[] for n in range(nodes)]
tree = set()

for _ in range(edges):
    edge_data = input().split()
    first, second, weight = int(edge_data[0]), int(edge_data[1]), int(edge_data[2])
    edge = Edge(first, second, weight)
    graph[first].append(edge)
    graph[second].append(edge)

    if len(edge_data) == 4:
        tree.add(first)
        tree.add(second)

pq = PriorityQueue()

for node in tree:
    for edge in graph[node]:
        pq.put(edge)

used_budget = 0

while not pq.empty():
    min_weight_edge = pq.get()
    non_tree_node = None

    if min_weight_edge.first not in tree and min_weight_edge.second in tree:
        non_tree_node = min_weight_edge.first
    elif min_weight_edge.first in tree and min_weight_edge.second not in tree:
        non_tree_node = min_weight_edge.second

    if non_tree_node is None:
        continue

    if min_weight_edge.weight + used_budget > budget:
        break

    used_budget += min_weight_edge.weight
    tree.add(non_tree_node)
    for edge in graph[non_tree_node]:
        pq.put(edge)

print(f"Budget used: {used_budget}")
