"""
Given a directed graph, we need to find all nodes that have no 'predecessors',
remove them from the graph one-by-one, and add them to a list in the order they are removed.

Input:
    Number of nodes -> 6

    For each node, there are the following children:
    Node A -> B, C
    Node B -> D, E
    Node C -> F
    Node D -> C, F
    Node E -> D
    Node F -> No children

    Here A is 'predecessor', B is child.
"""


def find_dependencies(graph):
    """
    Counting the predecessors for each node.
    Node having 0 predecessors will be removed.

    The valid return data represents a dictionary with:
    :key:   String, representing the node
    :value: Integer, representing the number of node's dependencies
    """
    result = {}
    for node, children in graph.items():
        if node not in result:
            result[node] = 0
        for child in children:
            if child not in result:
                result[child] = 1
            else:
                result[child] += 1

    return result


def find_node_without_dependencies(dependencies_by_node):
    """
    If a node without dependencies is not found,
    that means there is a cycle and the removal cannot continue.
    """
    for node, children in dependencies_by_node.items():
        if children == 0:
            return node
    return None


nodes = int(input())
graph = {}

for _ in range(nodes):

    # Processing the input data and adding it to the adjacency list (dictionary)
    # Valid data must be added to the list, for example: {'A': ['B', 'C']}
    node_data = input().split('->')
    node = node_data[0].strip()
    node_children = node_data[1].strip().split(', ') if node_data[1] else []
    graph[node] = node_children

dependencies_by_node = find_dependencies(graph)
has_cycles = False
sorted_nodes = []

while dependencies_by_node:
    node_to_remove = find_node_without_dependencies(dependencies_by_node)

    # If there is not a node without dependencies, the sorting cannot continue
    if node_to_remove is None:
        has_cycles = True
        break

    # Remove the first node with 0 dependencies
    dependencies_by_node.pop(node_to_remove)

    # Add that node to the collection with removed nodes
    sorted_nodes.append(node_to_remove)

    # Once the node is removed, update its children, so they depend on one node less
    for child in graph[node_to_remove]:
        dependencies_by_node[child] -= 1

if has_cycles:
    print("Invalid topological sorting")
else:
    print(f"Topological sorting: {', '.join(sorted_nodes)}")
