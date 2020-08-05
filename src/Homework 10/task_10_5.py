# task_10_5
"""Имеется текстовый файл. Все четные строки этого файла
записать во второй файл, а нечетные — в третий файл.
Порядок следования строк сохраняется."""

import open_file

text = open_file.file_open("task_10_5.txt", "r")

even_file = open("task_10_5_1.txt", "w")
uneven_file = open("task_10_5_2.txt", "w")

for i in range(len(text)):
    if i % 2 == 0:
        even_file.write(f"{text[i]}")
    else:
        uneven_file.write(f"{text[i]}")

even_file.close()
uneven_file.close()
