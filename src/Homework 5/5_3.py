# task_5_3
"""Два натуральных числа называют дружественными, если каждое из них
равно сумме всех делителей другого, кроме самого этого числа. Найти все
пары дружественных чисел, лежащих в диапазоне от 200 до 300."""

d = {}
for number in range(200, 301):
    summa = 0
    for i in range(1, number // 2 + 1):
        if number % i == 0:
            summa += i
    d[number] = summa
check = False

d_keys = list(d.keys())
d_values = list(d.values())

for key in d_keys:
    for value in d_values:
        index = d_values.index(value)
        if key == value and d[key] == d_keys[index]:
            print(f"{key} = {d[key]}")
            check = True
if not check:
    print("There aren't this numbers in this range")
