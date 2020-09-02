"""
Имеется текстовый файл.
Напечатать:
a) его первую строку;
b) его пятую строку;
c) его первые 5 строк;
d) его строки с s1-й по s2-ю;
e) весь файл.
"""
try:
    my_file = open('test.txt', 'r', encoding='utf8')
except FileNotFoundError:
    new_file = open('test.txt', 'w', encoding='utf8')
    new_file.close()
    my_file = open('test.txt', 'r', encoding='utf8')
lines = my_file.readlines()
my_file.close()
"""a) первая строка файла"""
print(lines[0])
"""b) пятая строка файла"""
print(lines[3])
"""c) первые пять строк файла"""
print(''.join(lines[0:5]))
"""d) строки 1:2 файла"""
print(''.join(lines[0:2]))
print(''.join(lines))
