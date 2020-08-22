from matrix_utils import matrix_classes, matrix_funcs


matrix = matrix_classes.Matrix(a=1, b=100)
matrix.gen_default_matrix()
print(matrix)
matrix_funcs.find_max_matrix_element(matrix)
matrix_funcs.find_min_matrix_element(matrix)
matrix_funcs.find_sum_matrix_elements(matrix)
