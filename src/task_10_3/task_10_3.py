"""
Имеется текстовый файл. Переписать в другой файл все
его строки с заменой в них символа 0 на символ 1 и
наоборот.
"""

with open('task_10_3.txt', 'r') as my_file:
    data = my_file.read()

result = []
for i in data:
    if i == '0':
        result.append('1')
    elif i == '1':
        result.append('0')
    else:
        result.append(i)

result_data = ''.join(result)

with open('task_10_3_result.txt', 'w') as output_file:
    output_file.write(result_data)
