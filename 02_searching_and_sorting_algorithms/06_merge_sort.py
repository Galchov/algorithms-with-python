"""
Worst-case complexity:       O(n * log n)
Average-case complexity:     O(n * log n)
Best-case complexity:        O(n * log n)
Worst-case space complexity: O(n)

Method:     Merging
Stability:  Yes
Optimal:    Yes
"""


def merge_arrays(left_side, right_side):
    result = [None] * (len(left_side) + len(right_side))

    result_index = 0
    right_index = 0
    left_index = 0

    while left_index < len(left_side) and right_index < len(right_side):
        if left_side[left_index] < right_side[right_index]:
            result[result_index] = left_side[left_index]
            left_index += 1
        else:
            result[result_index] = right_side[right_index]
            right_index += 1
        result_index += 1

    while left_index < len(left_side):
        result[result_index] = left_side[left_index]
        left_index += 1
        result_index += 1

    while right_index < len(right_side):
        result[result_index] = right_side[right_index]
        right_index += 1
        result_index += 1

    return result


def merge_sort(sequence):
    if len(sequence) == 1:
        return sequence

    middle_index = len(sequence) // 2
    left_side = sequence[:middle_index]
    right_side = sequence[middle_index:]

    return merge_arrays(merge_sort(left_side), merge_sort(right_side))


sequence = [int(x) for x in input().split()]


result = merge_sort(sequence)
print(*result, sep=' ')
