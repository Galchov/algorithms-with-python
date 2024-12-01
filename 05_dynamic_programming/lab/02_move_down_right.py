from collections import deque


def find_path(dp_matrix):
    result = deque()
    row = len(dp_matrix) - 1
    col = len(dp_matrix[0]) - 1

    while row > 0 and col > 0:
        result.appendleft([row, col])
        upper_item = dp_matrix[row - 1][col]
        left_item = dp_matrix[row][col - 1]
        if upper_item > left_item:
            row -= 1
        else:
            col -= 1

    for i in range(row, 0, -1):
        result.appendleft([i, col])

    for i in range(col, 0, -1):
        result.appendleft([row, i])

    result.appendleft([0, 0])
    return result


rows = int(input())
cols = int(input())

matrix = []
dp_matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])
    dp_matrix.append([0 for _ in range(cols)])

dp_matrix[0][0] = matrix[0][0]

for r in range(1):
    for c in range(1, cols):
        dp_matrix[r][c] = matrix[r][c] + dp_matrix[r][c - 1]

for c in range(1):
    for r in range(1, rows):
        dp_matrix[r][c] = matrix[r][c] + dp_matrix[r - 1][c]

for row in range(1, rows):
    for col in range(1, cols):
        current = matrix[row][col]
        upper = dp_matrix[row - 1][col]
        left = dp_matrix[row][col - 1]
        if current + upper > current + left:
            dp_matrix[row][col] = current + upper
        else:
            dp_matrix[row][col] = current + left


path = find_path(dp_matrix)
print(*path)
