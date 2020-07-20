#6) Задан целочисленный массив. Определить количество участков массива,
#на котором элементы монотонно возрастают (каждое следующее число
#больше предыдущего). [02-4.1-ML27]
import random
a= int(input ('Введите число цифр массиве: '))
list_a = [random.randint(0, 50) for el in range(a)]
print(list_a)
result=0
count=0
for j in range(len(list_a)-2):
    if list_a[j+2] > list_a[j+1] > list_a[j]:
        count+=1
    elif count>=1 and list_a[j+1] > list_a[j+2]:
        result+=1
        count=0
if list_a[-1] > list_a[-2] > list_a[-3]:
    result+=1
print(result)