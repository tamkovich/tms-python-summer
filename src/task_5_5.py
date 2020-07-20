# В массиве целых чисел с количеством элементов 19 определить максимальное
# число и заменить им все четные по значению элементы. [02-4.1-BL19]
myList = [i for i in range(1,19)]
m = max(myList)
for i in range(0, len(myList), 2):
    myList[i] = m
print(myList)
max(myList)
import random
lst = [random.randint(0, 20) for el in range(40)]
print(lst)
result=0
count=0
for j in range(len(lst)-2):
    if lst[j+2] > lst[j+1] > lst[j]:
        count+=1
    elif count>=1 and lst[j+1] > lst[j+2]:
        result+=1
        count=0
if lst[-1] > lst[-2] > lst[-3]:
    result+=1
print(result)
