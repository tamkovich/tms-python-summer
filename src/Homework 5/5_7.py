# task_5_7
"""Дана целочисленная квадратная матрица. Найти в каждой строке наи-
больший элемент и поменять его местами с элементом главной диагонали."""

import random


def output(tmp: list):
    """output matrix"""
    for i in tmp:
        for j in i:
            print(j, end='\t')
        print()


index = 0
min_value = input("Enter low limit for random: ")
max_value = input("Enter high limit for random: ")
size = input("Enter size of matrix: ")

try:
    min_value, max_value, size = int(min_value), int(max_value), int(size)
except TypeError:
    print("U should enter numbers")

matrix = [[random.randint(min_value, max_value) for i in range(size)]
          for j in range(size)]

print("Old matrix:")
output(matrix)

for i in range(size):
    max_value = max(matrix[i])
    for j in range(size):
        if max_value == matrix[i][j]:
            index = j
    matrix[i][i], matrix[i][index] = max_value, matrix[i][i]

print("New matrix:")
output(matrix)
