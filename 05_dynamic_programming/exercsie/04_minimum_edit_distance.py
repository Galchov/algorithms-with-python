replacement_cost = int(input())
insertion_cost = int(input())
deletion_cost = int(input())
first_str = input()
second_str = input()

rows = len(first_str) + 1
cols = len(second_str) + 1
results_table = []
[results_table.append([0] * cols) for _ in range(rows)]

for row in range(1, rows):
    results_table[row][0] = results_table[row - 1][0] + deletion_cost

for col in range(1, cols):
    results_table[0][col] = results_table[0][col - 1] + insertion_cost

for row in range(1, rows):
    for col in range(1, cols):
        if first_str[row - 1] == second_str[col - 1]:
            results_table[row][col] = results_table[row - 1][col - 1]
        else:
            results_table[row][col] = min(results_table[row - 1][col - 1] + replacement_cost,
                                          results_table[row - 1][col] + deletion_cost,
                                          results_table[row][col - 1] + insertion_cost)

print(f"Minimum edit distance: {results_table[rows - 1][cols - 1]}")
