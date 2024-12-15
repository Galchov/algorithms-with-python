"""
Input:
4
S.#.
.##E
.##.
....
Output:
8
"""


from collections import deque


def shortest_path_in_maze(n, maze):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    start = None
    end = None

    for i in range(n):
        for j in range(n):
            if maze[i][j] == 'S':
                start = (i, j)
            elif maze[i][j] == 'E':
                end = (i, j)

    queue = deque([(start[0], start[1], 0)])
    visited = set()
    visited.add(start)

    while queue:
        row, col, steps = queue.popleft()
        if (row, col) == end:
            return steps

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < n and 0 <= new_col < n and maze[new_row][new_col] != '#' and (new_row, new_col) not in visited:
                visited.add((new_row, new_col))
                queue.append((new_row, new_col, steps + 1))

    return -1


n = int(input())
maze = [input().strip() for _ in range(n)]

result = shortest_path_in_maze(n, maze)
print(result)
