"""
Имеется текстовый файл. Переписать в другой файл все
его строки с заменой в них символа 0 на символ 1 и
наоборот.
"""


my_file = open('test3.txt', 'r')
while True:
    new_file = []
    line = my_file.readline()
    if not line:
        break
    for i in line:
        if i == '1':
            new_file.append('0')
        elif i == '0':
            new_file.append('1')
        else:
            new_file.append(i)
    with open('test4.txt', 'a') as my_file2:
        my_file2.write(''.join(new_file))
my_file.close()
