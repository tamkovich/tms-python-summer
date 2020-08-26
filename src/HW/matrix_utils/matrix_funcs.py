from src.HW.matrix_utils.matrix_classes import Matrix


def find_max_matrix_element(matrix: Matrix) -> int or float:
    return max([max(i) for i in matrix.data])


def find_min_matrix_element(matrix: Matrix) -> int or float:
    return min([min(i) for i in matrix.data])


def find_sum_matrix_elements(matrix: Matrix) -> int or float:
    return sum([sum(i) for i in matrix.data])


if __name__ == '__main__':
    m1 = Matrix(5, 5, [-10, 10])
    print(str(m1))
    print(find_max_matrix_element(m1))
    print(find_min_matrix_element(m1))
    print(find_sum_matrix_elements(m1))
