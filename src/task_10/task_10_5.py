"""
Имеется текстовый файл. Все четные строки этого файла
записать во второй файл, а нечетные — в третий файл.
Порядок следования строк сохраняется.
"""

with open('test.txt', 'r') as f:
    file_odd = []
    file_even = []
    line = f.readlines()
    for i, el in enumerate(line):
        if i % 2 != 0:
            file_odd.append(el)
        else:
            file_even.append(el)
    with open('test5_odd.txt', 'w') as my_file2:
        my_file2.write(''.join(file_odd))
    with open('test5_even.txt', 'w') as my_file2:
        my_file2.write(''.join(file_even))
