# Создать текстовый файл и записать в него 6 строк.
# Записываемые строки вводятся с клавиатуры.

with open('task_10_1.txt', 'w') as my_file:
    for i in range(6):
        my_file.write(f'str N: {i} \n')
