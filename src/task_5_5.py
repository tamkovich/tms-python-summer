"""
В массиве целых чисел с количеством элементов 19 определить максимальное
число и заменить им все четные по значению элементы.
"""

import random

list_1 = []
count = 0
while count < 19:
    n = random.randint(1, 100)  # генерация 19-ти случайных элементов для списка
    list_1.append(n)
    count += 1

print(f'list_1:\n{list_1}')
max_el = max(list_1)
print(f'max elem: {max_el}')
print()
new_list = []
for i in list_1:
    if list_1.index(i) % 2 != 0:
        new_list.append(i)
    else:
        new_list.append(max_el)

print(f'new_list:\n{new_list}')
