"""
In practice, recursion is not needed for this solution,
it can be solved with iterative methods. This is just an exercise.
"""


def calculate_sum(numbers_list: list, idx: int):

    # Base case / Termination condition ->
    # The function will not stop and return the final result until this condition is True
    if idx == len(numbers_list) - 1:
        return numbers_list[idx]

    # Recursive call
    return numbers_list[idx] + calculate_sum(numbers_list, idx + 1)


numbers = [int(num) for num in input().split()]
print(calculate_sum(numbers, 0))
