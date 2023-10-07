# Write a function that accepts a square matrix (N x N 2D array) and returns
# the determinant of the matrix.

# How to take the determinant of a matrix -- it is simplest to start
# with the smallest cases:

# A 1x1 matrix |a| has determinant a.

# A 2x2 matrix [ [a, b], [c, d] ] or
# |a  b|
# |c  d|

# has determinant: a*d - b*c.

# The determinant of an n x n sized matrix is calculated by reducing
# the problem to the calculation of the determinants of n matrices
# ofn-1 x n-1 size.

# For the 3x3 case,
# [ [a, b, c],
# [d, e, f],
# [g, h, i]]

def sub_matrix(matrix, i, j) -> list[int, int]:
    '''
     remove i column and j row from matrix
    '''
    return [row[:j] + row[j+1:] for row in (matrix[:i] + matrix[i+1:])]


def determinant(matrix: list[int, int]):
    if len(matrix) == 1:
        return matrix[0][0]

    if len(matrix) == 2:
        if len(matrix[0]) == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    result = 0
    for i in range(len(matrix)):
        if i % 2 == 0:
            result += matrix[0][i] * determinant(sub_matrix(matrix, 0, i))
        else:
            result -= matrix[0][i] * determinant(sub_matrix(matrix, 0, i))

    return result


a = [[2, 4, 2],
     [3, 1, 1],
     [1, 2, 0]]
b = determinant(a)
print(b)
