def matrix_sum(matrix: list[list[int]]) -> tuple[int]:
    """
    Args:
        matrix (list): a matrix
    Returns:
        tuple[int]:
            the sum of the matrix's elements,
            the sum of the main diagonal,
            the sum of the reverse diagonal,
            the sum of the elements top of the main diagonal,
            the sum of the elements bottom of the main diagonal
            the sum of the elements top of the reverse diagonal,
            the sum of the elements bottom of the reverse diagonal
    """

    whole_sum = 0
    diagonal_sum = 0
    reverse_diagonal_sum = 0
    top_sum = 0
    bottom_sum = 0
    top_reverse_sum = 0
    bottom_reverse_sum = 0

    for index1, i in enumerate(matrix):
        for index2, j in enumerate(i):
            whole_sum += j
            if index1 == index2:
                diagonal_sum += j
            if index1 + index2 == len(matrix) - 1:
                reverse_diagonal_sum += j
            if index1 < index2:
                top_sum += j
            if index1 > index2:
                bottom_sum += j
            if index1 + index2 < len(matrix) - 1:
                top_reverse_sum += j
            if index1 + index2 > len(matrix) - 1:
                bottom_reverse_sum += j

    return (
        whole_sum,
        diagonal_sum,
        reverse_diagonal_sum,
        top_sum,
        bottom_sum,
        top_reverse_sum,
        bottom_reverse_sum,
    )


def matrix_max(matrix: list[list[int]]) -> tuple[int]:
    """
    Args:
        matrix (list): a matrix
    Returns:
        tuple:
            the max of the matrix's elements,
            the max of the main diagonal,
            the max of the elements top of the main diagonal,
            the max of the elements bottom of the main diagonal
    """
    whole_max = 0
    diagonal_max = 0
    top_max = 0
    bottom_max = 0

    for index1, i in enumerate(matrix):
        for index2, j in enumerate(i):
            whole_max = max(whole_max, j)
            if index1 == index2:
                diagonal_max = max(diagonal_max, j)
            if index1 < index2:
                top_max = max(top_max, j)
            if index1 > index2:
                bottom_max = max(bottom_max, j)

    return whole_max, diagonal_max, top_max, bottom_max


def two_sum(matrix1: list[list[int]], matrix2: list[list[int]]) -> list[list[int]]:
    """
    Args:
        matrix1 (list): a matrix
        matrix2 (list): a matrix
    Returns:
        list:
            the sum of the two matrices
    """

    sum_matrix = []

    for index1, i in enumerate(matrix1):
        row = []
        for index2, j in enumerate(i):
            row.append(j + matrix2[index1][index2])

        sum_matrix.append(row)

    return sum_matrix


def two_sub(matrix1: list[list[int]], matrix2: list[list[int]]) -> list[list[int]]:
    """
    Args:
        matrix1 (list): a matrix
        matrix2 (list): a matrix
    Returns:
        list:
            the subtraction of the two matrices
    """

    sub_matrix = []

    for index1, i in enumerate(matrix1):
        row = []
        for index2, j in enumerate(i):
            row.append(j - matrix2[index1][index2])

        sub_matrix.append(row)

    return sub_matrix


operation = input("Enter the operation: ")

i, j = map(int, input("Enter the dimensions of the matrix: ").split())

matrix = []

for n in range(i):
    row = []
    for m in range(j):
        row.append(int(input()))

    matrix.append(row)


for row in matrix:
    print("|", "   ".join(map(str, row)), "|")
    print("-   " * (len(row) + 3))


if operation == "sums":
    sums = matrix_sum(matrix)
    print("SUMS:")
    print(f"    The sum of the matrix's elements is {sums[0]}")
    print(f"    The sum of the main diagonal is {sums[1]}")
    print(f"    The sum of the reverse diagonal is {sums[2]}")
    print(f"    The sum of the elements top of the main diagonal is {sums[2]}")
    print(f"    The sum of the elements bottom of the main diagonal is {sums[3]}")
    print(f"    The sum of the elements top of the reverse diagonal is {sums[4]}")
    print(f"    The sum of the elements bottom of the reverse diagonal is {sums[5]}")
elif operation == "maxs":
    maxs = matrix_max(matrix)
    print("\nMAXS:")
    print(f"    The max of the matrix's elements is {maxs[0]}")
    print(f"    The max of the main diagonal is {maxs[1]}")
    print(f"    The max of the elements top of the main diagonal is {maxs[2]}")
    print(f"    The max of the elements bottom of the main diagonal is {maxs[3]}")
elif operation == "two_sum":
    while True:
        i1, j1 = map(int, input("Enter the dimensions of the second matrix: ").split())
        if i != i1 or j != j1:
            print("Matrices must have the same dimensions")
        else:
            break

    matrix2 = []

    for n in range(i1):
        row = []
        for m in range(j1):
            row.append(int(input()))

        matrix2.append(row)

    for row in matrix2:
        print("|", "   ".join(map(str, row)), "|")
        print("-   " * (len(row) + 3))

    sum_matrix = two_sum(matrix, matrix2)

    print("\nSUM MATRIX:")
    for row in sum_matrix:
        print("|", "   ".join(map(str, row)), "|")
        print("-   " * (len(row) + 3))
elif operation == "two_sub":
    while True:
        i1, j1 = map(int, input("Enter the dimensions of the second matrix: ").split())
        if i != i1 or j != j1:
            print("Matrices must have the same dimensions")
        else:
            break

    matrix2 = []

    for n in range(i1):
        row = []
        for m in range(j1):
            row.append(int(input()))

        matrix2.append(row)

    for row in matrix2:
        print("|", "   ".join(map(str, row)), "|")
        print("-   " * (len(row) + 3))

    sub_matrix = two_sub(matrix, matrix2)

    print("\nSUB MATRIX:")
    for row in sub_matrix:
        print("|", "   ".join(map(str, row)), "|")
        print("-   " * (len(row) + 3))
