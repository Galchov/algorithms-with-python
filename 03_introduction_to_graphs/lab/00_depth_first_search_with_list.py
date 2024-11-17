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
