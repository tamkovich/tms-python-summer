"""
Задание 10.01
Имеется текстовый файл. Напечатать:
a) его первую строку;
b) его пятую строку;
c) его первые 5 строк;
d) его строки с s1-й по s2-ю;
e) весь файл.
"""

with open('test.txt', 'r') as f:
    line = f.readlines()
    print(line[0])
    print(line[4])
    print(line[:5])
    print(line[3:5])
    print(line)

with open('test.txt') as my_file:
    for line in my_file.readlines():
        print(line)
