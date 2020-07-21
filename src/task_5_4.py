n = int(input())
summa = 0
for i in range(n+1):
    if i != 0:
        x = (1 / i)
        summa += x
    elif i == 0:
        continue
print(summa)
