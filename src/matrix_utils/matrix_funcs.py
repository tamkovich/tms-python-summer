from matrix_utils.matrix_classes import Matrix


def find_max_matrix_element(matrix: Matrix) -> int or float:
    return max(map(max, matrix._data))


def find_min_matrix_element(matrix: Matrix) -> int or float:
    return min(map(min, matrix._data))


def find_sum_matrix_elements(matrix: Matrix) -> int or float:
    result = 0
    for elem in matrix._data:
        for number in elem:
            result += number
    return result


