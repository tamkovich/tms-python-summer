# 5) В массиве целых чисел с количеством элементов 19 определить максимальное
# число и заменить им все четные по значению элементы. [02-4.1-BL19]
list_a = []
import random
a = 0
while a < 19:
    list_a.append(random.randint(0, 1000))
    a += 1
print(list_a)
max(list_a)
print(max(list_a))
for j in range(0, 19):
    if j % 2 == 0:
        list_a[j] = max(list_a)
print(list_a)
