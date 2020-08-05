# task_10_4
"""Имеется текстовый файл. Переписать в другой файл все
его строки с заменой в них символа 0 на символ 1 и
наоборот."""

import open_file

text = open_file.file_open("task_10_4.txt", "r")

# для очистки файла
f = open("new_task_10_4.txt", "w")
f.close()

for line in text:
    list_of_lines = []
    for el in line:
        list_of_lines.append("0" if el == "1" else "1" if el == "0" else el)
    new_str = "".join(list_of_lines)

    with open("new_task_10_4.txt", "a") as f:
        f.write(new_str)
