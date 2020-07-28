"""
Дана целочисленная квадратная матрица. Найти в каждой строке наи-
больший элемент и поменять его местами с элементом главной диагонали.
"""
import random

a = []  # квадратная матрица
n = int(input(":"))  # количество рядов/столбцов в матрице a

for i in range(n):
    vloj_spisok = []
    for j in range(n):
        vloj_spisok.append(random.randint(0, 100))
    a.append(vloj_spisok)
print(f'Enter matrix:\n{a}')

for i, el in enumerate(a):
    tmp_max = el.index(max(el))  # индекс максимального элемента в строке
    a[i][i], a[i][tmp_max] = max(el), a[i][i]

print(f'new matrix:\n{a}')

