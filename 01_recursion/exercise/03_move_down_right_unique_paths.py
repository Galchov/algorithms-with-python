def count_unique_paths(row, col, rows, cols):
    """
    Given a matrix size, the task is to start from its first cell (row = 0 and col = 0)
    and reach the bottom right corner (row = rows - 1 and col = cols - 1).
    Based on the size of the matrix, there will be various possible paths to reach the target point,
    so the Backtracking algorithm is for finding all unique paths from the start to the end.
    """

    # Check if you go out of the matrix / invalid index
    # As we move only right and down, there are checks only for positive indices
    # If that's the case return 0 paths completed and continue to the next possible cell
    if row >= rows or col >= cols:
        return 0

    # Check if the current position matches the bottom right corner of the matrix
    # This is the target point for path completion
    # Return 1 path completed
    if row == rows - 1 and col == cols - 1:
        return 1

    # Storing the amount of successfully completed paths
    result = 0

    # Move Right
    result += count_unique_paths(row, col + 1, rows, cols)
    # Move Down
    result += count_unique_paths(row + 1, col, rows, cols)

    # This is when 1 path is completed, but the function is going backwards now to continue with the checks
    return result


def alternative_solution(rows, cols):
    """
    This is more direct approach -> breaking the problem to smaller problems until reaching the smallest.
    The return result will be combination of all problems starting from the smallest found.
    """

    if rows == 1 or cols == 1:
        return 1
    else:
        return alternative_solution(rows, cols - 1) + alternative_solution(rows - 1, cols)


rows = int(input())
cols = int(input())


print(count_unique_paths(0, 0, rows, cols))
print(alternative_solution(rows, cols))
