"""
The input is an expression, containing a ternary conditional operator '?:',
in the following format: "{boolean value} ? {result if the value is true} : {result if it's false}".

The results values will always be digits and the boolean value will be represented as 't' or 'f'.

For example:
Input   -> "t ? 4 : 2"
Result  -> "4"
The boolean value says, it's True, so the output is the value on the left.

Input   -> "f ? t ? 4 : 2 : 1"
Output  -> "1"
The boolean value says False, so we don't go into the inner expression, but the right-side value
(f ? (t ? 4 : 2) : 1)

In the solution, the problem is broken down into smaller ones where that's possible, using Recursion.
"""


def process_expression(expression, index):

    # This is the bottom, and the program can enter this line only after a recursive call,
    # and only if the problem is broken down to the last part where there are
    # no more booleans, but a digit.
    if expression[index].isdigit():
        return expression[index]

    # The first thing we check is, whether the boolean is True or False
    if expression[index] == 't':

        # If it is True, a recursive call is made to enter the expression left-side value,
        # as the task's requirement is
        return process_expression(expression, index + 2)

    # The program reaches this point if the boolean is False
    # This new variable will help to find the index of '?' symbol as start,
    # and then iterate until we reach equal amount between '?' and ':'.
    # ':' means that, the program will reach the right-side value, which is the False result
    current_index = index + 1

    # This variable confirms the amount of '?' and ':' is equal, when reaches 0 during the loop
    conditional_statement_status = 0

    while True:
        if expression[current_index] == '?':
            conditional_statement_status += 1
        elif expression[current_index] == ':':
            conditional_statement_status -= 1

            # When 0 is reached, the program makes another recursive call,
            # this time with the False result
            if conditional_statement_status == 0:
                return process_expression(expression, current_index + 1)

        current_index += 1


expression = input().split()

print(process_expression(expression, 0))
