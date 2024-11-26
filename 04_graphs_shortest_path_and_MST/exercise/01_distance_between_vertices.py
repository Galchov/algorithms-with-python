from collections import deque


def find_path(start_node, destination_node, graph):
    visited = {}
    queue = deque()

    visited[start_node] = None
    queue.append(start_node)

    while queue:
        current_node = queue.popleft()

        if current_node == destination_node:
            path = []

            while current_node:
                path.append(current_node)
                current_node = visited[current_node]
            return path

        for child in graph[current_node]:
            if child not in visited:
                visited[child] = current_node
                queue.append(child)


nodes = int(input())
pairs = int(input())

graph = {}

for _ in range(nodes):
    source_str, children_str = input().split(':')
    source = int(source_str)
    children = [int(x) for x in children_str.split()] if children_str else []
    graph[source] = children

for _ in range(pairs):
    start_node_str, destination_node_str = input().split('-')
    start_node = int(start_node_str)
    destination_node = int(destination_node_str)

    result = find_path(start_node, destination_node, graph)

    if result:
        print(f"{{{start_node}, {destination_node}}} -> {len(result) - 1}")
    else:
        print(f"{{{start_node}, {destination_node}}} -> -1")
