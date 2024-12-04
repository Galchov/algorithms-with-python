first_str = input()
second_str = input()

results_table = []
rows = len(first_str) + 1
cols = len(second_str) + 1

for _ in range(rows):
    results_table.append([0] * cols)

for row in range(1, rows):
    results_table[row][0] = results_table[row - 1][0] + 1

for col in range(1, cols):
    results_table[0][col] = results_table[0][col - 1] + 1

for i in range(rows - 1):
    for j in range(cols - 1):
        first = first_str[i]
        second = second_str[j]
        if first_str[i] == second_str[j]:
            results_table[i + 1][j + 1] = results_table[i][j]
        else:
            results_table[i + 1][j + 1] = min(results_table[i + 1][j], results_table[i][j + 1]) + 1


print(f"Deletions and Insertions: {results_table[rows - 1][cols - 1]}")
