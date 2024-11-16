"""
Worst-case complexity:       O(n^2)         -> Big-O: When the pivot element is either greatest or the smallest element
Average-case complexity:     O(n * log n)   -> Big-omega: When the pivot element is always the middle or near the middle
Best-case complexity:        O(n * log n)   -> Big-theta: When the above conditions do not occur
Worst-case space complexity: O(log n)

Method:     Partitioning
Stability:  No
Optimal:    Yes
"""


def quick_sort(start_index, end_index, sequence):
    if start_index >= end_index:
        return

    pivot_index = start_index
    left_index = start_index + 1
    right_index = end_index

    while left_index <= right_index:
        if sequence[left_index] > sequence[pivot_index] > sequence[right_index]:
            sequence[left_index], sequence[right_index] = sequence[right_index], sequence[left_index]
        if sequence[left_index] <= sequence[pivot_index]:
            left_index += 1
        if sequence[right_index] >= sequence[pivot_index]:
            right_index -= 1

    sequence[pivot_index], sequence[right_index] = sequence[right_index], sequence[pivot_index]

    quick_sort(start_index, right_index - 1, sequence)
    quick_sort(left_index, end_index, sequence)


sequence = [int(x) for x in input().split()]


quick_sort(0, len(sequence) - 1, sequence)
print(*sequence, sep=' ')
