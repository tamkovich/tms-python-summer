# В массиве целых чисел с количеством элементов 19 определить максимальное
# число и заменить им все четные по значению элементы.
from random import randint

mlist = [randint(0, 100) for i in range(19)]
max_num = max(mlist)
for index, value in enumerate(mlist):
    if value % 2 == 0:
        mlist[index] = max_num
print(mlist)
