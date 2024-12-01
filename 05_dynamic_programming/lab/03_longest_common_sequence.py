from collections import deque


first_str = input()
second_str = input()

rows = len(first_str) + 1
cols = len(second_str) + 1

dp_matrix = []
[dp_matrix.append([0] * cols) for _ in range(rows)]

for row in range(1, rows):
    for col in range(1, cols):
        if first_str[row - 1] == second_str[col - 1]:
            prev = dp_matrix[row - 1][col - 1]
            dp_matrix[row][col] = prev + 1
        else:
            up = dp_matrix[row - 1][col]
            left = dp_matrix[row][col - 1]
            dp_matrix[row][col] = max(up, left)


letters_seq = deque()
row = rows - 1
col = cols - 1

while row >= 0 and col >= 0:
    if first_str[row - 1] == second_str[col - 1]:
        letters_seq.appendleft(first_str[row - 1])
        row -= 1
        col -= 1
    elif dp_matrix[row - 1][col] > dp_matrix[row][col - 1]:
        row -= 1
    else:
        col -= 1

print(dp_matrix[rows - 1][cols - 1])
