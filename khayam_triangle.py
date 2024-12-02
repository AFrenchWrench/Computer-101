def generate_pascals_triangle(n):

    """
    Generate Pascal's triangle up to the nth row.

    Args:
        n (int): The number of rows in the triangle.

    Returns:
        list: A list of lists, where each sublist is a row in the triangle.
    """

    triangle = []

    for i in range(n):
        row = [1]
        for j in range(1, i):
            element = triangle[i - 1][j - 1] + triangle[i - 1][j]
            row.append(element)
        if i > 0:
            row.append(1)
        triangle.append(row)

    return triangle


def print_pascals_triangle(triangle):

    for row in triangle:
        print(" ".join(map(str, row)))


n = int(input())

triangle = generate_pascals_triangle(n)

print_pascals_triangle(triangle)
