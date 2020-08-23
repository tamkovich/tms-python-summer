from task_13.matrix_utils.matrix_classes import Matrix


def find_max_matrix_element(matrix: Matrix) -> int or float:
    return max(map(max, matrix.data))


def find_min_matrix_element(matrix: Matrix) -> int or float:
    return min(map(min, matrix.data))


def find_sum_matrix_elements(matrix: Matrix) -> int or float:
    return sum(map(sum, matrix.data))
