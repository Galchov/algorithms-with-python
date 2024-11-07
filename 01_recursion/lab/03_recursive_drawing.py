"""
In practice, recursion is not needed for this solution,
it can be solved with iterative methods. This is just an exercise.
"""


def draw_mirror_figure(n):

    # Base case / Bottom
    if n <= 0:
        return

    # Pre-recursive behavior
    print('*' * n)

    # Recursive call
    draw_mirror_figure(n - 1)

    # Post recursive behavior
    print('#' * n)


n = int(input())

draw_mirror_figure(n)
