from matrix_utils.matrix_classes import Matrix


def max_element(matrix: Matrix) -> int or float:
    """
    Find max element in the matrix
    :param matrix: matrix
    :return: max element of matrix
    """
    return max(map(max, matrix.data))


def min_element(matrix: Matrix) -> int or float:
    """
    Find min element in the matrix
    :param matrix: matrix
    :return: min element of matrix
    """
    return min(map(min, matrix.data))


def sum_of_elements(matrix: Matrix) -> int or float:
    """
    Find sum of all elements in matrix
    :param matrix: matrix
    :return: sum of elements
    """
    return sum(map(sum, matrix.data))
