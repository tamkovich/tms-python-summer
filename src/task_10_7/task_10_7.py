"""Создать матрицу случайных чисел и сохранить ее в json
файл. После прочесть ее, обнулить все четные элементы
и сохранить в другой файл"""

import json
from random import randint

matrix = [[randint(-100, 100) for i in range(10)] for j in range(10)]

with open('task_10_7_1.txt', 'w') as my_file:
    json.dump(matrix, my_file)

with open('task_10_7_1.txt', 'r') as my_file:
    data = [[j for j in i if j % 2 == 0] for i in json.load(my_file)]

with open('task_10_7_2.txt', 'w') as my_file:
    json.dump(data, my_file)

