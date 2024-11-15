"""
Worst-case complexity:       O(n^2) -> If you want to sort in ascending order, but the list is in descending order
Average-case complexity:     O(n^2) -> When the elements in the list are in jumbled order
Best-case complexity:        O(n)   -> Occurs when the list is already sorted
Worst-case space complexity: O(1)   -> If you use extra variable (for swapping, indexing, boolean...),
                                       or if there are two or more, complexity could go to O(2) respectively

Method:     Exchanging
Stability:  Yes -> Maintains the order of equal elements
Optimal:    No
"""


def bubble_sort(sequence):
    for i in range(len(sequence)):
        for j in range(1, len(sequence) - i):
            if sequence[j - 1] > sequence[j]:
                sequence[j], sequence[j - 1] = sequence[j - 1], sequence[j]


def bubble_sort_while_loop(sequence):
    i = 0
    is_sorted = False

    while not is_sorted:
        is_sorted = True
        for j in range(1, len(sequence) - i):
            if sequence[j - 1] > sequence[j]:
                sequence[j], sequence[j - 1] = sequence[j - 1], sequence[j]
                is_sorted = False

        i += 1


sequence = [int(x) for x in input().split()]


# bubble_sort(sequence)
bubble_sort_while_loop(sequence)
print(*sequence, sep=' ')
