# Для заданного числа N составьте программу вычисления суммы
# S=1+1/2+1/3+1/4+...+1/N, где N – натуральное число. [02-3.2-ML21]
n = int(input("Enter a natural number:"))
if n == 0:
    print("Error. Enter number != 0")

summ = 0
for i in range (1, abs(n) + 1):
    k = 1 / i
    summ += k

print(summ)