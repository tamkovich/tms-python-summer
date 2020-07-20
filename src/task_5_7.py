# Дана целочисленная квадратная матрица. Найти в каждой строке наибольший
# элемент и поменять его местами с элементом главной диагонали.
from random import randint

matrix = [[randint(0, 100) for i in range(4)] for i in range(4)]
print(matrix)
for i, value in enumerate(matrix):
    tmp = matrix[i][i]
    tmp_max = value.index(max(value))
    matrix[i][i] = max(value)
    matrix[i][tmp_max] = tmp

print(matrix)
