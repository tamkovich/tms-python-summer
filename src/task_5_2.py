x = input()
size_x = len(x)
x = int(x)
summa = 0
proizv = 1
for i in range(size_x):
    y = (x % 10)
    summa += y
    proizv *= y
    x = x // 10
print('summa =', summa)
print('proizvedenie =', proizv)
