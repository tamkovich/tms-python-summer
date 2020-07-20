# Задан целочисленный массив. Определить количество участков массива,
# на котором элементы монотонно возрастают (каждое следующее число
# больше предыдущего).

from random import randint

mlist = [randint(0, 100) for i in range(25)]
counter = 0
size = len(mlist)
for index, value in enumerate(mlist):
    if value == (size - 1):
        break
    if mlist[index - 1] >= value < mlist[index + 1]:
        counter += 1
print(f"Лист: {mlist}")
print(f"Количество монотонно возраствющих участков: {counter}")
