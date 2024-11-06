"""
In practice, recursion is not needed for this solution,
it can be solved with iterative methods. This is just an exercise.
"""


def calculate_factorial(num: int):

    # Base case
    if num <= 1:
        return num

    # Recursive call
    return num * calculate_factorial(num - 1)


number = int(input())

print(calculate_factorial(number))
