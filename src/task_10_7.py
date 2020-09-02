"""
Создать матрицу случайных чисел и сохранить ее в json файл.
После прочесть ее, обнулить все четные элементы и сохранить в другой файл
"""
from random import randint
import json

random_numbs = [[randint(1, 100) for i in range(4)] for j in range(4)]
with open('test.json', 'w') as my_file:
    data = json.dumps(random_numbs)
    my_file.write(data)
with open('test.json') as my_file:
    data = json.loads(my_file.read())
    print(data)
    for i, value in enumerate(data):
        for index, value1 in enumerate(value):
            if value1 % 2 == 0:
                data[i][index] = 0
    with open('test1.json', 'w') as new_file:
        data1 = json.dumps(data)
        new_file.write(data1)
    with open('test1.json') as my_file1:
        data = json.loads(my_file1.read())
        print(data)