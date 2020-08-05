from random import randint
import json

matrix = [[randint(1, 9) for i in range(5)] for j in range(5)]

with open('task_10_7_1.json', 'w') as my_file:
    data = json.dumps(matrix)
    my_file.write(data)

with open('task_10_7_1.json') as my_file:
    data = json.loads(my_file.read())
    print(data)
    for i, value in enumerate(data):
        for index, value_1 in enumerate(value):
            if value_1 % 2 == 0:
                data[i][index] = 0

with open('task_10_7_1.json', 'w') as new_file:
    data1 = json.dumps(data)
    new_file.write(data1)
with open('task_10_7_1.json') as my_file1:
    data = json.loads(my_file1.read())
    print(data)
