# task_10_7
"""Создать матрицу случайных чисел и сохранить ее в json
файл. После прочесть ее, обнулить все четные элементы
и сохранить в другой файл"""
import json
import random

size = input("Enter size of matrix: ")
min_value = input("Enter min value for random: ")
max_value = input("Enter max value for random: ")

try:
    size, min_value, max_value = int(size), int(min_value), int(max_value)
except ValueError:
    print("Not a number")

matrix = [[random.randint(min_value, max_value)
           for i in range(size)] for j in range(size)]

with open("task_10_7.txt", "w") as f:
    f.write(json.dumps({"Matrix": matrix}))

with open("task_10_7.txt", "r") as f:
    data = json.loads(f.read())
    value = data["Matrix"]
    with open("new_task_10_7.txt", "w") as new_file:
        for i in range(size):
            for j in range(size):
                if (i + j) % 2 == 0:
                    value[i][j] = 0
        new_file.write(json.dumps({"New matrix": value}))
