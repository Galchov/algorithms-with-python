"""
This is an example of a Backtracking algorithm that finds and prints
all possible ways to go from a start point to an end point in a given matrix with
randomly placed obstacles within, that will challenge the movement,
so the algorithm has to bypass them.
"""


def find_all_paths(row, col, maze, direction, path):

    # Check for a valid index. Cannot exceed the size of the matrix
    if row < 0 or col < 0 or row >= len(maze) or col >= len(maze[0]):
        return

    # Check if there is a wall on the way - Invalid move
    if maze[row][col] == '*':
        return

    # Check if the cell is already visited - Invalid move
    if maze[row][col] == 'v':
        return

    # Keep track on the path you have gone through
    path.append(direction)

    # If reaching the target point / exit, stop the movement
    if maze[row][col] == 'e':
        # Print the path
        print(''.join(path))
    else:
        # Mark the current cell as visited
        maze[row][col] = 'v'

        # Move Up
        find_all_paths(row - 1, col, maze, 'U', path)
        # Move Down
        find_all_paths(row + 1, col, maze, 'D', path)
        # Move Left
        find_all_paths(row, col - 1, maze, 'L', path)
        # Move Right
        find_all_paths(row, col + 1, maze, 'R', path)

        # After going back, set the cell from 'v' (visited) to '-' (empty)
        maze[row][col] = '-'

    # On the way back, remove the direction
    path.pop()


rows = int(input())
columns = int(input())

the_maze = [list(input()) for _ in range(rows)]

find_all_paths(0, 0, the_maze, '', [])
