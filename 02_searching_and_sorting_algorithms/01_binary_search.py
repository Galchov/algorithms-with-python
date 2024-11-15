"""
Binary search is an algorithm that finds the position of a target value
within a sorted array.

Worst-case complexity:       O(log n)
Average-case complexity:     O(log n)
Best-case complexity:        O(1)
Worst-case space complexity: O(1)

Optimal: Yes
"""


def binary_search(sequence, target_element):
    # Identify the two borders of the search
    start_index = 0
    end_index = len(sequence) - 1

    # Check if the end index/border is below zero.
    # That means the given list is empty and the functions cannot continue
    if end_index < start_index:
        return -1

    while start_index <= end_index:
        # Find the middle index that will divide the list into two parts,
        # so you can search only one of them in the next round
        middle_index = (start_index + end_index) // 2
        middle_element = sequence[middle_index]

        # If the element is found, function ends successfully
        if middle_element == target_element:
            return sequence.index(target_element)

        # Checking, which side the target element is located at,
        # and continuing to search only there
        elif middle_element < target_element:
            start_index = middle_index + 1
        else:
            end_index = middle_index - 1

    # If the element is not found, function ends unsuccessfully
    return -1


sequence = [int(x) for x in input().split()]
target_element = int(input())


print(binary_search(sequence, target_element))
