# Дана целочисленная квадратная матрица. Найти в каждой строке наи-
# больший элемент и поменять его местами с элементом главной диагонали.

import random


def square_matrix_creator(n: int) -> list:
    matrix = []
    for i in range(n):
        tmp = []
        for j in range(n):
            tmp.append(random.randint(0, 100))
        matrix.append(tmp)

    return matrix

def task_executor(matrix: list):
    max_value = 0
    for i in range(len(matrix)):
        matrix_string = matrix[i]
        max_value = max(matrix_string)
        max_val_index = matrix_string.index(max_value)
        matrix[i][i], matrix[i][max_val_index] = max_value, matrix[i][i]





my_matrix = [
    [1,2,3],
    [1,2,3],
    [1,2,3],
]

print(my_matrix)
task_executor(my_matrix)
print(my_matrix)

my_matrix_2 = square_matrix_creator(4)
print(my_matrix_2)
task_executor(my_matrix_2)
print(my_matrix_2)
