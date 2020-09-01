from matrix_utils.matrix_classes import Matrix
import numpy as np

def find_max_matrix_element(matrix: Matrix) -> int:
    """
    find max elem in matrix
    :param matrix: matrix
    :return: int
    """
    return (max(map(max, matrix.data)))

def find_min_matrix_element(matrix: Matrix) -> int:
    """
    find min elem in matrix
    :param matrix: matrix
    :return: int
    """
    return (min(map(min, matrix.data)))

def find_sum_matrix_elements(matrix: Matrix) -> int:
    """
    find sum elements in matrix
    :param matrix: matrix
    :return: int
    """
    return np.sum(matrix.data)
