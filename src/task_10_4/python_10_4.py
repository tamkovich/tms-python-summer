"""Имеется текстовый файл. Все четные строки этого файла
записать во второй файл, а нечетные — в третий файл.
Порядок следования строк сохраняется."""

with open('task_10_4.txt', 'r') as my_file:
    line = my_file.readline()
    count = 0
    odd_str_list = []
    even_str_list = []
    while line:
        if count % 2 == 0:
            even_str_list.append(line)
        else:
            odd_str_list.append(line)
        count += 1
        line = my_file.readline()

odd_str = ''.join(odd_str_list)
even_str = ''.join(even_str_list)

with open('task_10_4_odd_lines.txt', 'w') as odd_str_file:
    odd_str_file.write(odd_str)

with open('task_10_4_even_lines.txt', 'w') as even_str_file:
    even_str_file.write(even_str)
