from collections import deque

nums_seq = [int(x) for x in input().split()]

size = len(nums_seq)

results_table = []
[results_table.append([1] * size) for _ in range(2)]

previous = []
[previous.append([None] * size) for _ in range(2)]

best_size = 0
best_row = 0
best_col = 0

for curr_idx in range(1, size):
    curr_num = nums_seq[curr_idx]

    for prev_idx in range(curr_idx):
        prev_num = nums_seq[prev_idx]

        if curr_num > prev_num and results_table[0][curr_idx] < results_table[1][prev_idx] + 1:
            results_table[0][curr_idx] = results_table[1][prev_idx] + 1
            previous[0][curr_idx] = prev_idx

        if prev_num > curr_num and results_table[1][curr_idx] < results_table[0][prev_idx] + 1:
            results_table[1][curr_idx] = results_table[0][prev_idx] + 1
            previous[1][curr_idx] = prev_idx

    if results_table[0][curr_idx] > best_size:
        best_size = results_table[0][curr_idx]
        best_row = 0
        best_col = curr_idx
    if results_table[1][curr_idx] > best_size:
        best_size = results_table[1][curr_idx]
        best_row = 1
        best_col = curr_idx

result = deque()

while best_col is not None:
    result.appendleft(nums_seq[best_col])
    best_col = previous[best_row][best_col]
    best_row = 1 if best_row == 0 else 0

print(*result, sep=' ')
