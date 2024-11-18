# Example graph with 6 nodes

# Matrix - Each cell keeps whether and how nodes are connected.
# Can be represented with True or False as well, instead 0 and 1.
adjacency_matrix = [
    [0, 0, 0, 1, 0, 0, 1],  # node 0 -> Connection to nodes: 3 and 6
    [0, 0, 1, 1, 1, 1, 1],  # node 1 -> Connection to nodes: 2, 3, 4, 5 and 6
    [0, 1, 0, 0, 1, 1, 0],  # node 2 -> Connection to nodes: 1, 4 and 5
    [1, 1, 0, 0, 0, 1, 0],  # node 3 -> Connection to nodes: 0, 1 and 5
    [0, 1, 1, 0, 0, 0, 1],  # node 4 -> Connection to nodes: 1, 2 and 6
    [0, 1, 1, 1, 0, 0, 0],  # node 5 -> Connection to nodes: 1, 2 and 3
    [1, 1, 0, 0, 1, 0, 0],  # node 6 -> Connection to nodes: 0, 1 and 4
]

# Dictionary - The key is a node and the value is a list of its neighbours
adjacency_list_as_dictionary = {
    0: [3, 6],
    1: [2, 3, 4, 5, 6],
    2: [1, 4, 5],
    3: [0, 1, 5],
    4: [1, 2, 6],
    5: [1, 2, 3],
    6: [0, 1, 4],
}

# List/Array - 2D list where each node is a list with its neighbours in it
# and its value is its actual index within the outer list.
adjacency_list = [
    [3, 6],             # node 0
    [2, 3, 4, 5, 6],    # node 1
    [1, 4, 5],          # node 2
    [0, 1, 5],          # node 3
    [1, 2, 6],          # node 4
    [1, 2, 3],          # node 5
    [0, 1, 4],          # node 6
]

# Edge list - A list of edges, where each edge is represented as a pair (tuple) of nodes.
edge_list = [
    (0, 3),  # Node 0 is connected to node 3
    (0, 6),  # Node 0 is connected to node 6
    (1, 2),  # Node 1 is connected to node 2
    (1, 3),  # Node 1 is connected to node 3
    (1, 4),  # Node 1 is connected to node 4
    (1, 5),  # Node 1 is connected to node 5
    (1, 6),  # Node 1 is connected to node 6... and so on for each node...
    (2, 1),
    (2, 4),
    (2, 5),
    (3, 0),
    (3, 1),
    (3, 5),
    (4, 1),
    (4, 2),
    (4, 6),
    (5, 1),
    (5, 2),
    (5, 3),
    (6, 0),
    (6, 1),
    (6, 4),
]
