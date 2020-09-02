from task_13.matrix_utils import matrix_classes
from task_13.matrix_utils import matrix_funcs

if __name__ == "__main__":
    matrix = matrix_classes.Matrix(5, 5, 4, 9)
    print(matrix)
    print(matrix_funcs.find_max_matrix_element(matrix))
    print(matrix_funcs.find_min_matrix_element(matrix))
    print(matrix_funcs.find_sum_matrix_elements(matrix))
