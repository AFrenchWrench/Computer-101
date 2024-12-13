from math import inf


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


def is_diagonal(matrix: list[list[int]]) -> bool:
    """
    Args:
        matrix (list): a matrix
    Returns:
        bool:
            True if the matrix is diagonal, False otherwise
    """
    for index1, i in enumerate(matrix):
        for index2, j in enumerate(i):
            if index1 != index2:
                if j != 0:
                    return False
    return True


def is_upper_triangular(matrix: list[list[int]]) -> bool:
    """
    Args:
        matrix (list): a matrix
    Returns:
        bool:
            True if the matrix is upper triangular, False otherwise
    """
    for index1, i in enumerate(matrix):
        for index2, j in enumerate(i):
            if index1 > index2:
                if j != 0:
                    return False
    return True


def is_lower_triangular(matrix: list[list[int]]) -> bool:
    """
    Args:
        matrix (list): a matrix
    Returns:
        bool:
            True if the matrix is lower triangular, False otherwise
    """
    for index1, i in enumerate(matrix):
        for index2, j in enumerate(i):
            if index1 < index2:
                if j != 0:
                    return False
    return True


def is_symmetric(matrix: list[list[int]]) -> bool:
    """
    Args:
        matrix (list): a matrix
    Returns:
        bool:
            True if the matrix is symmetric, False otherwise
    """
    for index1, i in enumerate(matrix):
        for index2, j in enumerate(i):
            if matrix[index2][index1] != j:
                return False
    return True


def first_row_sum(matrix: list[list[int]]) -> int:
    """
    Args:
        matrix (list): a matrix
    Returns:
        int:
            the sum of the first row of the matrix
    """
    return sum(matrix[0])


def last_column_product(matrix: list[list[int]]) -> int:
    """
    Args:
        matrix (list): a matrix
    Returns:
        int:
            the product of the last column of the matrix
    """
    p = 1

    for i in matrix:
        p *= i[-1]

    return p


def min_on_reverse_diagonal(matrix: list[list[int]]) -> int:
    """
    Args:
        matrix (list): a matrix
    Returns:
        int:
            the minimum element of the reverse diagonal
    """
    min_on_reverse = inf

    for index1, i in enumerate(matrix):
        for index2, j in enumerate(i):
            if index1 + index2 == len(matrix) - 1:
                min_on_reverse = min(min_on_reverse, j)

    return min_on_reverse


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


def zero_counts(matrix: list[list[int]]) -> int:
    """
    Args:
        matrix (list): a matrix
    Returns:
        int:
            the number of zeros in the matrix
    """

    count = 0

    for i in matrix:
        for j in i:
            if j == 0:
                count += 1

    return count


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


def two_mul(matrix1: list[list[int]], matrix2: list[list[int]]) -> list[list[int]]:
    """
    Args:
        matrix1 (list): a matrix
        matrix2 (list): a matrix
    Returns:
        list:
            the multiplication of the two matrices
    """

    mul_matrix = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            element = 0
            for k in range(len(matrix1[0])):
                element += matrix1[i][k] * matrix2[k][j]
            row.append(element)
        mul_matrix.append(row)
    return mul_matrix


if __name__ == "__main__":
    operation = input("Enter the operation: ")

    i, j = map(int, input("Enter the dimensions of the matrix: ").split())

    matrix = []

    for n in range(i):
        row = []
        while len(row) != j:
            row = list(
                map(int, input(f"Enter the elements of the row {n + 1}: ").split())
            )
            if len(row) != j:
                print("The number of elements is not equal to the number of columns")
            else:
                break

        matrix.append(row)

    print("-" * 10)
    for row in matrix:
        print(*row)
    print("-" * 10)

    if operation == "sums":
        sums = matrix_sum(matrix)
        print("SUMS:")
        print(f"    The sum of the matrix's elements is {sums[0]}")
        print(f"    The sum of the main diagonal is {sums[1]}")
        print(f"    The sum of the reverse diagonal is {sums[2]}")
        print(f"    The sum of the elements top of the main diagonal is {sums[2]}")
        print(f"    The sum of the elements bottom of the main diagonal is {sums[3]}")
        print(f"    The sum of the elements top of the reverse diagonal is {sums[4]}")
        print(
            f"    The sum of the elements bottom of the reverse diagonal is {sums[5]}"
        )
    elif operation == "maxs":
        maxs = matrix_max(matrix)
        print("\nMAXS:")
        print(f"    The max of the matrix's elements is {maxs[0]}")
        print(f"    The max of the main diagonal is {maxs[1]}")
        print(f"    The max of the elements top of the main diagonal is {maxs[2]}")
        print(f"    The max of the elements bottom of the main diagonal is {maxs[3]}")
    elif operation == "is_diagonal":
        if is_diagonal(matrix):
            print("The matrix is diagonal")
        else:
            print("The matrix is not diagonal")
    elif operation == "is_upper_triangular":
        if is_upper_triangular(matrix):
            print("The matrix is upper triangular")
        else:
            print("The matrix is not upper triangular")
    elif operation == "is_lower_triangular":
        if is_lower_triangular(matrix):
            print("The matrix is lower triangular")
        else:
            print("The matrix is not lower triangular")
    elif operation == "is_symmetric":
        if is_symmetric(matrix):
            print("The matrix is symmetric")
        else:
            print("The matrix is not symmetric")
    elif operation == "first_row_sum":
        print(f"The sum of the first row is {first_row_sum(matrix)}")
    elif operation == "last_column_product":
        print(f"The product of the last column is {last_column_product(matrix)}")
    elif operation == "zero_counts":
        print(f"The number of zeros in the matrix is {zero_counts(matrix)}")
    elif operation == "min_on_reverse_diagonal":
        print(
            f"The minimum element on the reverse diagonal is {min_on_reverse_diagonal(matrix)}"
        )
    elif operation == "two_sum":
        while True:
            i1, j1 = map(
                int, input("Enter the dimensions of the second matrix: ").split()
            )
            if i != i1 or j != j1:
                print("Matrices must have the same dimensions")
            else:
                break

        matrix2 = []

        for n in range(i1):
            row = []
            while len(row) != j1:
                row = list(
                    map(int, input(f"Enter the elements of the row {n + 1}: ").split())
                )
                if len(row) != j1:
                    print(
                        "The number of elements is not equal to the number of columns"
                    )
                else:
                    break

            matrix2.append(row)

        print("-" * 10)
        for row in matrix2:
            print(*row)
        print("-" * 10)

        sum_matrix = two_sum(matrix, matrix2)

        print("\nSUM MATRIX:")
        print("-" * 10)
        for row in sum_matrix:
            print(*row)
        print("-" * 10)
    elif operation == "two_sub":
        while True:
            i1, j1 = map(
                int, input("Enter the dimensions of the second matrix: ").split()
            )
            if i != i1 or j != j1:
                print("Matrices must have the same dimensions")
            else:
                break

        matrix2 = []

        for n in range(i1):
            row = []
            while len(row) != j1:
                row = list(
                    map(int, input(f"Enter the elements of the row {n + 1}: ").split())
                )
                if len(row) != j1:
                    print(
                        "The number of elements is not equal to the number of columns"
                    )
                else:
                    break

            matrix2.append(row)

        print("-" * 10)
        for row in matrix2:
            print(*row)
        print("-" * 10)

        sub_matrix = two_sub(matrix, matrix2)

        print("\nSUB MATRIX:")
        print("-" * 10)
        for row in sub_matrix:
            print(*row)
        print("-" * 10)
    elif operation == "two_mul":
        while True:
            i1, j1 = map(
                int, input("Enter the dimensions of the second matrix: ").split()
            )
            if j != i1:
                print(
                    "Second matrix's rows must be equal to the first matrix's columns"
                )
            else:
                break

        matrix2 = []

        for n in range(i1):
            row = []
            while len(row) != j1:
                row = list(
                    map(int, input(f"Enter the elements of the row {n + 1}: ").split())
                )
                if len(row) != j1:
                    print(
                        "The number of elements is not equal to the number of columns"
                    )
                else:
                    break

            matrix2.append(row)

        print("-" * 10)
        for row in matrix2:
            print(*row)
        print("-" * 10)

        mul_matrix = two_mul(matrix, matrix2)

        print("\nMUL MATRIX:")
        print("-" * 10)
        for row in mul_matrix:
            print(*row)
        print("-" * 10)
    elif operation == "are_equal":
        while True:
            i1, j1 = map(
                int, input("Enter the dimensions of the second matrix: ").split()
            )
            if i != i1 or j != j1:
                print("Matrices must have the same dimensions")
            else:
                break

        matrix2 = []

        for n in range(i1):
            row = []
            while len(row) != j1:
                row = list(
                    map(int, input(f"Enter the elements of the row {n + 1}: ").split())
                )
                if len(row) != j1:
                    print(
                        "The number of elements is not equal to the number of columns"
                    )
                else:
                    break

            matrix2.append(row)

        print("-" * 10)
        for row in matrix2:
            print(*row)
        print("-" * 10)

        if matrix == matrix2:
            print("The matrices are equal")
        else:
            print("The matrices are not equal")
