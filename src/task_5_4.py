# Для заданного числа N составьте программу вычисления суммы
# S=1+1/2+1/3+1/4+...+1/N, где N – натуральное число
while True:
    n = input("\ninput natural numb: ")
    if n == "q":
        break
    if not n.isdigit():
        print("input only digit!")
        continue
    n = int(n)
    s = 1

    for i in range(2, n + 2):
        s += 1 / i
        print(s)
