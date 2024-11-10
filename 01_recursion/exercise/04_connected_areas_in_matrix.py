class Area:
    def __init__(self, row: int, col: int, size: int) -> None:
        self.row = row
        self.col = col
        self.size = size


def find_connected_area(row, col, matrix):
    """
    Given a matrix and a starting point (0, 0 by default), this function finds all the areas within the matrix,
    makerd with '-'. The borders are recognized by two factors - marked with '*' or end of the matrx (invalid index).

    The possible moves to mark the area territory are Up, Down, Right and Left. Every time an area is discovered,
    i.e., all cells between the borders are iterated, the function adds 1 to the counter.

    At the end the functions returns the total count of the areas found.

    Example:
        rows = 4
        columns = 9

        The matrix:
        ---*---*-
        ---*---*-
        ---*---*-
        ----*-*--

    The result is 3. Reached after iterating over all the cells that are '-', and are surrounded with 4 borders.
    """

    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
        return 0
    if matrix[row][col] == '*' or matrix[row][col] == 'v':
        # Or matrix[row][col] != '-':
        return 0

    matrix[row][col] = 'v'
    result = 1

    # Move Up
    result += find_connected_area(row - 1, col, matrix)
    # Move Right
    result += find_connected_area(row, col + 1, matrix)
    # Move Down
    result += find_connected_area(row + 1, col, matrix)
    # Move Left
    result += find_connected_area(row, col - 1, matrix)

    return result


rows = int(input())
cols = int(input())

matrix = []

for _ in range(rows):
    matrix.append(list(input()))

areas = []
for row in range(rows):
    for col in range(cols):
        size = find_connected_area(row, col, matrix)
        if size == 0:
            continue
        areas.append(Area(row, col, size))

print(f"Total areas found: {len(areas)}")
for index, area in enumerate(sorted(areas, key=lambda a: a.size, reverse=True)):
    print(f"Area #{index + 1} at ({area.row}, {area.col}), size: {area.size}")
