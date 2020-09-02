"""
Имеется текстовый файл. Все четные строки этого файла записать во второй
файл, а нечетные — в третий файл. Порядок следования строк сохраняется.
"""
try:
    my_file = open('test.txt', 'r', encoding='utf8')
except FileNotFoundError:
    print('File not found!')
new_file1 = open('test1.txt', 'w', encoding='utf8')
new_file2 = open('test2.txt', 'w', encoding='utf8')
for line in my_file.readlines():
    if len(line) % 2 == 0:
        new_file1.write(line)
    else:
        new_file2.write(line)

my_file.close()
new_file1.close()
