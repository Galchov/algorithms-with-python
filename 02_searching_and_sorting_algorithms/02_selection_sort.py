"""
Worst-case complexity:       O(n^2) -> If you want to sort in ascending order, but the list is in descending order
Average-case complexity:     O(n^2) -> When the elements in the list are in jumbled order
Best-case complexity:        O(n^2) -> Occurs when the list is already sorted
Worst-case space complexity: O(1)   -> Because of the extra variable 'current_min_idx'

Method:     Selection
Stability:  No -> Rearranges the equal elements in unpredictable order
Optimal:    No
"""


def selection_sort(sequence):
    # Starting from the first element in the sequence
    for i in range(len(sequence)):
        current_min_idx = i
        # Looping over the elements right of the first
        for j in range(i + 1, len(sequence)):
            # Check if the current element in the inner loop is smaller than the outer loop's current element
            if sequence[j] < sequence[current_min_idx]:
                # And set the index of the minimum to the current inner
                current_min_idx = j

        # Pythonic swap
        sequence[i], sequence[current_min_idx] = sequence[current_min_idx], sequence[i]


sequence = [int(x) for x in input().split()]

selection_sort(sequence)
print(*sequence, sep=' ')
