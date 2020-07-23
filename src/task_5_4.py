"""
Для заданного числа N составьте программу вычисления суммы
S=1+1/2+1/3+1/4+...+1/N, где N – натуральное число.
"""

n = int(input("N: "))
if n == 0:
    print("Error by zero")  # исключаем деление на ноль

summ = 0
for i in range(1, abs(n) + 1):
    k = 1 / i
    summ += k

print(f'S: {summ}')
