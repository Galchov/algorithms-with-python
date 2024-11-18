def dfs(node, graph, visited, component):
    if visited[node]:
        return

    visited[node] = True
    for neighbour in graph[node]:
        dfs(neighbour, graph, visited, component)

    component.append(node)


nodes = int(input())
graph = []

for node in range(nodes):
    line = input()
    neighbours = [] if line == '' else [int(x) for x in line.split()]
    graph.append(neighbours)

visited = [False] * nodes

for node in range(nodes):
    if visited[node]:
        continue
    component = []
    dfs(node, graph, visited, component)
    print(f"Connected component: {' '.join(str(c) for c in component)}")
