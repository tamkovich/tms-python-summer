# Задан целочисленный массив. Определить количество участков массива,
# на котором элементы монотонно возрастают (каждое следующее число
# больше предыдущего). [02-4.1-ML27]
import random
lst = [random.randint(0, 10) for el in range(10)]
print(lst)
for i, el in enumerate(lst):
    if i == len(lst) - 1:
        break
    if el > lst[i+1]:
        print(str(el) + ' больше чем следующее ' + str(lst[i+1]))
    else:
        print(str(el) + ' не больше чем следующее ' + str(lst[i+1]))