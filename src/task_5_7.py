#7) Дана целочисленная квадратная матрица. Найти в каждой строке наибольший элемент и поменять его местами с элементом
# главной диагонали.[02-4.2-ML22]
import random
n = int(input())
l = []
list_a = [random.randint(0, 50) for el in range(n)]
for i in range(n):
    list_a = []
    for j in range(n):
        j = j + random.randint(0, 50)
        list_a.append(j)
    x = max(list_a)
    y = list_a[i]
    indeks = list_a.index(x)
    del list_a[i]
    list_a.insert(i, x)
    del list_a[indeks]
    list_a.insert(indeks, y)
    l.append(list_a)
for i in l:
    print(i)