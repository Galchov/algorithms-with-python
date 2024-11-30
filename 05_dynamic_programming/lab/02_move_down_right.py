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

# TODO: Track the path backwards from the end (bottom right) to the start (top left), and print its indices
