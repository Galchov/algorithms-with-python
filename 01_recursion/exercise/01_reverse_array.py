"""
Only for the purpose of the exercise in this example is used Recursion.

For such problem a recursive solution is not required at all.
"""


def reverse_array(index, arr):
    if index >= len(arr) // 2:
        return ' '.join(arr)

    start_index = index
    end_index = len(arr) - start_index - 1
    arr[start_index], arr[end_index] = arr[end_index], arr[start_index]
    return reverse_array(start_index + 1, arr)


def iterative_reverse(arr):
    for i in range(len(arr) // 2):
        end_index = len(arr) - i - 1
        arr[i], arr[end_index] = arr[end_index], arr[i]

    return arr


arr = input().split()

print(reverse_array(0, arr))
