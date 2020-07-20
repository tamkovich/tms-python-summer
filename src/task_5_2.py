x = int(input("введите число: "))
summa = 0

proizvedenie = 1

while x > 0:
    ostatok = x % 10
    summa = summa + ostatok
    proizvedenie = proizvedenie * ostatok
    x = x // 10

print("сумма числа равна: ", summa)
print("произведение числа равна: ", proizvedenie)
