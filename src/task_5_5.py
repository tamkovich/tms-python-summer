# 5) В массиве целых чисел с количеством элементов 19 определить максимальное
# число и заменить им все четные по значению элементы.
myList = [i for i in range(1,19)]
m = max(myList)
for i in range(0, len(myList), 2):
    myList[i] = m
print(myList)
