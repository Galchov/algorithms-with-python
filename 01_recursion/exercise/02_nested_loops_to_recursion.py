"""
Backtracking algorithm that generates all possible permutations of given number -> n,
starting from 1 to n, stored in a list.

When the algorithm reaches a dead end (the end of the list), it goes one step back and
checks for other possible solution. When it finds all possible solutions, it again goes
one step back and does the same so on until all solutions are found.

Every time a solution is find, it prints it on a single line.
"""


def generate_permutations(index, nums):

    # Base case -> Dead end
    # It prints the found result and continues the function to the next step
    if index >= len(nums):
        print(*nums, sep=' ')
        return

    # Recursive call within the loop, which finds
    # all the possible solution of the current branch
    for num in range(1, len(nums) + 1):
        nums[index] = num
        generate_permutations(index + 1, nums)


n = int(input())
nums = [None] * n

generate_permutations(0, nums)
