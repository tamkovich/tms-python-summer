 # 4) Для заданного числа N составьте программу вычисления суммы
 # S=1+1/2+1/3+1/4+...+1/N, где N – натуральное число.

n = input("введите натуральное число = ")
summa = 0
try:
    n = int(n)
    for i in range(1, n + 1):
        summa += 1 / i
    print(summa)
except:
    print('некоректный ввод')