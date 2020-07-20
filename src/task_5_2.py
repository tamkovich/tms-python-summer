# Дано число. Найти сумму и произведение его цифр.
x = input("X: ")
if not x.isdigit():
    print("is not digit!")
_sum = 0
mult = 1
for i in x:
    _sum += int(i)
    mult *= int(i)
print(f"Сумма = {_sum}\nПроизведение = {mult}")
