from collections import deque

sequence = input().split()

size = [0] * len(sequence)
previous = [None] * len(sequence)

best_size = 0
best_idx = 0

for curr_idx in range(len(sequence)):
    curr_word = sequence[curr_idx]
    curr_len = len(curr_word)
    curr_size = 1
    prev = None

    for prev_idx in range(curr_idx - 1, -1, -1):
        prev_word = sequence[prev_idx]
        prev_len = len(prev_word)

        if prev_len >= curr_len:
            continue

        if size[prev_idx] + 1 >= curr_size:
            curr_size = size[prev_idx] + 1
            prev = prev_idx

    size[curr_idx] = curr_size
    previous[curr_idx] = prev

    if curr_size > best_size:
        best_size = curr_size
        best_idx = curr_idx

longest_string_chain = deque()
index = best_idx

while index is not None:
    longest_string_chain.appendleft(sequence[index])
    index = previous[index]

print(*longest_string_chain, sep=' ')
