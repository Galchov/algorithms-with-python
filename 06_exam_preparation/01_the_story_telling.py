def dfs(node, graph, visited, ord_story):
    if node in visited:
        return node

    visited.add(node)
    for child in graph[node]:
        dfs(child, graph, visited, ord_story)

    ord_story.append(node)


def topological_sort(graph):
    visited = set()
    ordered_story = []

    for node in graph:
        if node not in visited:
            dfs(node, graph, visited, ordered_story)

    return ordered_story


story = input()

graph = {}

while story != "End":
    story_data = story.split('->')
    node = story_data[0].strip()
    children = story_data[1].split()
    graph[node] = children

    story = input()

result = topological_sort(graph)
while result:
    print(result.pop(), end=' ')
