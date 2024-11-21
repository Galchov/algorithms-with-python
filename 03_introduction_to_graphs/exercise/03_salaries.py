"""
Given a directed graph, represented as a matrix where nodes are the inner lists and
their edges are represented by 'Y' on its index of direction. In the example below: Node 1 with edges
directed to Nodes 0, 2 and 5.

The task is to find the total value of all Nodes. Every Node has value the sum of its children,
as a Node without any children has value of 1. In the example below, Node 0 is not directed to any other Node,
so its value is 1.

The DFS algorith iterates over all Nodes recursively until reaches a dead end (Node without children) and
calculates the sum going backwards.

Step 1: Node 0 -> No children = Value 1
Step 2: Node 1 -> Children [0, 2, 5]
Step 3: Node 1 -> Iterate over first child 0, returns value of 1
Step 3: Node 1 -> Iterate over child 2, finds its children [0, 5]
...And so on until all Nodes are checked and their values calculated.

Input:
    6
    NNNNNN -> Node 0
    YNYNNY -> Node 1
    YNNNNY -> Node 2
    NNNNNN -> Node 3
    YNYNNN -> Node 4
    YNNYNN -> Node 5
Output:
    17
"""


def dfs(node, graph, values):

    # Check, if the current Node's value has already been found
    # and return it, if it is
    if values[node] is not None:
        return values[node]

    # Check, if this is the last node (without children)
    # and return 1 as its value. Also update it in the values list.
    if len(graph[node]) == 0:
        values[node] = 1
        return 1

    # Track the value of the current node
    value = 0

    for child in graph[node]:

        # Recursion call is made for each child of the current node
        value += dfs(child, graph, values)

    # Update the value in the values list on the current node's index
    values[node] = value
    return value


nodes = int(input())

graph = []

for _ in range(nodes):
    line = list(input())
    children = []
    for index, state in enumerate(line):
        if state == 'Y':
            children.append(index)
    graph.append(children)

# Keep the values of each node by matching index
values = [None] * nodes
total_values = 0

for node in range(nodes):
    total_values += dfs(node, graph, values)

print(total_values)
