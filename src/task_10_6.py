"""
Имеются два текстовых файла с одинаковым числом строк. Выяснить,
совпадают ли их строки. Если нет, то получить номер первой строки,
в которой эти файлы отличаются друг от друга.
"""
try:
    my_file = open('test1.txt', 'rt', encoding='utf8')
    my_file2 = open('test2.txt', 'rt', encoding='utf8')
except FileNotFoundError:
    print('File not found!')
tmp = my_file2.readlines()
for index, value in enumerate(my_file.readlines()):
    if value != tmp[index]:
        print(f'{index + 1} - \ntext1: {value}text2: {tmp[index]}')
