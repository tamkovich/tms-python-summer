"""
Имеется текстовый файл. Переписать в другой файл все его
строки с заменой в них символа 0 на символ 1 и наоборот.
"""
try:
    my_file = open('test.txt', 'r', encoding='utf8')
except FileNotFoundError:
    print('File not found!')
new_file = open('test1.txt', 'w', encoding='utf8')
for line in my_file.readlines():
    tmp = []
    for i in line:
        tmp.append("0" if i == "1" else "1" if i == "0" else i)
    new_file.write(''.join(tmp))
my_file.close()
new_file.close()
