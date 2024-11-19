def dfs(symbol, row, col, matrix, visited):
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
        return

    if visited[row][col]:
        return

    if matrix[row][col] != symbol:
        return

    visited[row][col] = True

    # Move Down
    dfs(symbol, row + 1, col, matrix, visited)
    # Move Left
    dfs(symbol, row - 1, col, matrix, visited)
    # Move Up
    dfs(symbol, row, col - 1, matrix, visited)
    # Move Right
    dfs(symbol, row, col + 1, matrix, visited)


rows = int(input())
cols = int(input())

matrix = []
visited = []

for _ in range(rows):
    matrix.append(list(input()))
    visited.append([False] * cols)

areas = {}

for row in range(rows):
    for col in range(cols):
        symbol = matrix[row][col]
        if visited[row][col]:
            continue
        dfs(symbol, row, col, matrix, visited)
        if symbol not in areas:
            areas[symbol] = 1
        else:
            areas[symbol] += 1


total_areas = 0
for value in areas.values():
    total_areas += value

print(f"Areas: {total_areas}")
for key, value in sorted(areas.items()):
    print(f"Letter '{key}' -> {value}")
