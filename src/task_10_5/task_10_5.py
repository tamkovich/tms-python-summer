"""Имеется текстовый файл. Напечатать:
a) его первую строку;
b) его пятую строку;
c) его первые 5 строк;
d) его строки с s1-й по s2-ю;
e) весь файл."""

with open('task_10_5.txt', 'r') as my_file:
    strings = []
    line = my_file.readline()
    while line:
        strings.append(line)
        line = my_file.readline()
    # a)
    print('a):')
    print(strings[0], end='')
    # b)
    print('b):')
    print(strings[4], end='')
    # c)
    print('c):')
    for i in range(5):
        print(strings[i], end='')
    # d)
    print('d):')
    for i in range(2, 4 + 1):
        print(strings[i], end='')
    # e)
    print('e):')
    print(''.join(strings))
