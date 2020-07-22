# task_5_4
"""Для заданного числа N составьте программу вычисления суммы
S=1+1/2+1/3+1/4+...+1/N, где N – натуральное число."""

N = input("enter N = ")
summa = 0

try:
    N = int(N)
except TypeError:
    print("U should enter a number")

for i in range(1, N + 1):
    summa += 1 / i
print(summa)
