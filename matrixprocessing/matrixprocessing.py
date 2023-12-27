"""Pythagoras: is a useful program to use"""


def read_matrix():
    rows, columns = map(int, input("Enter matrix size: ").split())
    print("Enter matrix:")
    matrix = [list(map(float, input().split())) for _ in range(rows)]
    return matrix, rows, columns


def add_matrices(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        return None
    return [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]


def multiply_by_constant(matrix, constant):
    return [[elem * constant for elem in row] for row in matrix]


def multiply_matrices(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        return None
    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result


def determinant(matrix):
    size = len(matrix)
    if size == 1:
        return matrix[0][0]
    elif size == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for j in range(size):
        minor = [row[:j] + row[j + 1:] for row in matrix[1:]]
        det += (-1) ** j * matrix[0][j] * determinant(minor)

    return det


def inverse_matrix(matrix):
    size = len(matrix)
    identity = [[0 if i != j else 1 for j in range(size)] for i in range(size)]
    augmented_matrix = [row + identity_row for row, identity_row in zip(matrix, identity)]

    for i in range(size):
        max_row = max(range(i, size), key=lambda j: abs(augmented_matrix[j][i]))
        augmented_matrix[i], augmented_matrix[max_row] = augmented_matrix[max_row], augmented_matrix[i]

        pivot = augmented_matrix[i][i]
        if pivot == 0:
            return None
        for j in range(i, size * 2):
            augmented_matrix[i][j] /= pivot

        for k in range(size):
            if k != i:
                multiplier = augmented_matrix[k][i]
                for j in range(i, size * 2):
                    augmented_matrix[k][j] -= multiplier * augmented_matrix[i][j]

    inverse = [row[size:] for row in augmented_matrix]
    return inverse


def transpose_main(matrix):
    return [list(row) for row in zip(*matrix)]


def transpose_side(matrix):
    return [list(row)[::-1] for row in zip(*matrix[::-1])]


def transpose_vertical(matrix):
    return [row[::-1] for row in matrix]


def transpose_horizontal(matrix):
    return matrix[::-1]


while True:
    print("1. Add matrices")
    print("2. Multiply matrix by a constant")
    print("3. Multiply matrices")
    print("4. Transpose matrix")
    print("5. Calculate a determinant")
    print("6. Inverse matrix")
    print("0. Exit")
    choice = input("Your choice: ")

    if choice == "0":
        break
    elif choice == "1":
        matrix1, rows1, columns1 = read_matrix()
        matrix2, rows2, columns2 = read_matrix()
        if rows1 != rows2 or columns1 != columns2:
            print("Matrices have different sizes. Addition is not possible.")
            continue
        result = add_matrices(matrix1, matrix2)
        if result is None:
            print("Matrices have different sizes. Addition is not possible.")
        else:
            print("The result is:")
            print(result)
    elif choice == "2":
        matrix, rows, columns = read_matrix()
        constant = float(input("Enter the constant: "))
        result = multiply_by_constant(matrix, constant)
        print("The result is:")
        print(result)
    elif choice == "3":
        matrix1, rows1, columns1 = read_matrix()
        matrix2, rows2, columns2 = read_matrix()
        if columns1 != rows2:
            print("Matrices cannot be multiplied. Invalid sizes.")
            continue
        result = multiply_matrices(matrix1, matrix2)
        if result is None:
            print("Matrices cannot be multiplied. Invalid sizes.")
        else:
            print("The result is:")
            print(result)
    elif choice == "4":
        transpose_options = {
            "1": transpose_main,
            "2": transpose_side,
            "3": transpose_vertical,
            "4": transpose_horizontal
        }
        print("1. Main diagonal")
        print("2. Side diagonal")
        print("3. Vertical line")
        print("4. Horizontal line")
        transpose_choice = input("Your choice: ")
        matrix, rows, columns = read_matrix()
        if transpose_choice in transpose_options:
            result = transpose_options[transpose_choice](matrix)
            print("The result is:")
            print(result)
        else:
            print("Invalid choice for transpose.")
    elif choice == "5":
        matrix, rows, columns = read_matrix()
        if rows != columns:
            print("The matrix is not square. Determinant can't be calculated.")
            continue
        result = determinant(matrix)
        print("The result is:")
        print(result)
    elif choice == "6":
        matrix, rows, columns = read_matrix()
        if rows != columns:
            print("The matrix is not square. Inverse matrix can't be calculated.")
            continue
        det = determinant(matrix)
        if det == 0:
            print("This matrix doesn't have an inverse.")
            continue
        result = inverse_matrix(matrix)
        if result is None:
            print("This matrix doesn't have an inverse.")
        else:
            print("The result is:")
            for row in result:
                print(*row)
    else:
        print("Invalid choice")
