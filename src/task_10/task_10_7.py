"""
Создать матрицу случайных чисел и сохранить ее в json
файл. После прочесть ее, обнулить все четные элементы
и сохранить в другой файл
"""


from random import randint
n = 5
m = 4
matrix = [[randint(10, 99) for j in range(n)] for i in range(m)]
data = {
    1: matrix,
}

import json
with open("data_matrix.json", "w") as write_file:
    json.dump(data, write_file)
with open("data_matrix.json", "r") as read_file:
    json_content = read_file.read()
    data1 = json.loads(json_content)
    matrix_data = data1.values()  # извлечение данных по ключу из json
    for m in matrix_data:
        matrix1 = m  # извлечение матрицы из value
    print(matrix1)
    for i, element in enumerate(matrix1):
        for j, el in enumerate(element):
            if j % 2 == 0:
                matrix1[i][j] = 0
    print(matrix1)

data_zeromatrix = {
    1: matrix1
}
with open("data_matrix1.json", "w") as write_file1:
    json.dump(data_zeromatrix, write_file1)
