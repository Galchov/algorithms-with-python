cables_a = [int(x) for x in input().split()]
size = len(cables_a) + 1

cables_b = [c for c in range(1, size)]

results_table = []
[results_table.append([0] * size) for _ in range(size)]

for row in range(1, size):
    for col in range(1, size):
        if cables_a[row - 1] == cables_b[col - 1]:
            results_table[row][col] = results_table[row - 1][col - 1] + 1
        else:
            results_table[row][col] = max(results_table[row - 1][col], results_table[row][col - 1])

print(f"Maximum pairs connected: {results_table[size - 1][size - 1]}")
