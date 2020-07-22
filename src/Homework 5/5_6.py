# task_5_6
"""Задан целочисленный массив. Определить количество участков массива,
на котором элементы монотонно возрастают (каждое следующее число
больше предыдущего)."""

import random

min_value = input("Enter low limit for random: ")
max_value = input("Enter high limit for random: ")
size = input("Enter size of list: ")

try:
    min_value, max_value, size = int(min_value), int(max_value), int(size)
except TypeError:
    print("U should enter numbers")

l = [random.randint(min_value, max_value) for i in range(size)]
count, result = 0, 0
check = False
print(f"List: {l}")

for i in range(size - 1):
    if l[i] < l[i + 1]:
        check = True
        continue

    if check and l[i] > l[i + 1]:
        result += 1
    check = False
print(f"Numbers = {result}")
