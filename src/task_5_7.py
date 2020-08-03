# Дана целочисленная квадратная матрица. Найти в каждой строке наибольший
# элемент и поменять его местами с элементом главной диагонали.[02-4.2-ML22]
from random import randint

matrix = [[randint(0, 100) for i in range(4)] for i in range(4)]
print(matrix)
for i, value in enumerate(matrix):
    index = value.index(max(value))
    matrix[i][i], matrix[i][index] = matrix[i][index], matrix[i][i]

print(matrix)