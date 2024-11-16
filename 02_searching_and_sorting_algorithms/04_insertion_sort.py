"""
Worst-case complexity:       O(n^2) -> If you want to sort in ascending order, but the list is in descending order
Average-case complexity:     O(n^2) -> When the elements in the list are in jumbled order
Best-case complexity:        O(n)   -> Occurs when the list is already sorted
Worst-case space complexity: O(1)   -> Because of an extra variable

Method:     Insertion
Stability:  Yes
Optimal:    No
"""


def insertion_sort(sequence):
    for i in range(1, len(sequence)):
        j = i
        while sequence[j] < sequence[j - 1] and j > 0:
            sequence[j], sequence[j - 1] = sequence[j - 1], sequence[j]
            j -= 1


sequence = [int(x) for x in input().split()]


insertion_sort(sequence)
print(*sequence,sep=' ')
