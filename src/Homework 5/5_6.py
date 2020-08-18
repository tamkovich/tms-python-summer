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

list_of_numbers = [random.randint(min_value, max_value) for i in range(size)]
count, result = 0, 0
check = False
print(f"List: {list_of_numbers}")

for i in range(size - 1):
    if list_of_numbers[i] < list_of_numbers[i + 1]:
        check = True
        continue

    if check and list_of_numbers[i] > list_of_numbers[i + 1]:
        result += 1
    check = False
print(f"Numbers = {result}")
