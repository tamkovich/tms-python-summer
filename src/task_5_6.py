# 6) Задан целочисленный массив. Определить количество участков массива,
# на котором элементы монотонно возрастают (каждое следующее число
# больше предыдущего)
import random
lst = [random.randint(0, 20) for el in range(10)]
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
