# task_5_5
"""В массиве целых чисел с количеством элементов 19 определить максимальное
число и заменить им все четные по значению элементы."""

import random

min_value = input("Enter low limit for random: ")
max_value = input("Enter high limit for random: ")

try:
    min_value, max_value = int(min_value), int(max_value)
    l = [random.randint(min_value, max_value) for i in range(19)]
    print(f"Old list: {l}")

    max_el = max(l)
    print(f"Max element: {max_el}")

    for i in range(19):
        if i % 2 == 0:
            l[i] = max_el
    print(f"New list: {l}")
except TypeError:
    print("U should enter numbers")
