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
    tmp = a[i][i]  # элементы диагонали матрицы
    tmp_max = el.index(max(el))  # индекс максимального элемента в строке
    a[i][i] = max(el)
    a[i][tmp_max] = tmp

print(f'new matrix:\n{a}')

