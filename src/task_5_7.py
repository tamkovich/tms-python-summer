# Дана целочисленная квадратная матрица. Найти в каждой строке наи-
# больший элемент и поменять его местами с элементом главной диагонали.
# [02-4.2-ML22]
import random

def output(tmp: list):
    for i in tmp:
        for j in i:
            print(j, end='\t')
        print()
index = 0
min_value = input("Введите нижний придел рандома: ")
max_value = input("Введите верхний придел рандома: ")
size = input("Введите размер матрицы: ")

try:
    min_value, max_value, size = int(min_value), int(max_value), int(size)
    matrix = [[random.randint(min_value, max_value) for i in range(size)] for j in range(size)]

    print("старая матрица:")
    output(matrix)

    for i in range(size):
        max_value = matrix[i][0]
        index = 0
        for j in range(size):
            if max_value < matrix[i][j]:
                max_value = matrix[i][j]
                index = j
        matrix[i][i], matrix[i][index] = max_value, matrix[i][i]

    print("Новвая матрица:")
    output(matrix)
except:
    print("Некоректный ввод!Вводите только цифы.")