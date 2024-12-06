from collections import deque

sequence = [int(x) for x in input().split()]

length = [0] * len(sequence)
previous = [0] * len(sequence)

best_len = 0
best_idx = -1

for current_idx in range(len(sequence)):
    current_el = sequence[current_idx]
    current_len = 1
    current_prev = -1

    for prev_idx in range(current_idx - 1, -1, -1):
        prev_el = sequence[prev_idx]
        prev_len = length[prev_idx]
        if current_el > prev_el and prev_len + 1 >= current_len:
            current_len = prev_len + 1
            current_prev = prev_idx

    length[current_idx] = current_len
    previous[current_idx] = current_prev

    if current_len > best_len:
        best_len = current_len
        best_idx = current_idx

longest_incr_subseq = deque()
index = best_idx

while index != -1:
    longest_incr_subseq.appendleft(sequence[index])
    index = previous[index]

print(*longest_incr_subseq, sep=' ')
