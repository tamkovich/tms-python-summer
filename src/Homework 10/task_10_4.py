# task_10_4
"""Имеется текстовый файл. Переписать в другой файл все
его строки с заменой в них символа 0 на символ 1 и
наоборот."""

with open("task_10_4.txt", "r") as f:
    text = f.readlines()

# для очистки файла
f = open("new_task_10_4.txt", "w")
f.close()

for line in text:
    list_of_line = []
    for symbol in line:
        if symbol == "0":
            symbol = "1"
        elif symbol == "1":
            symbol = "0"
        list_of_line.append(symbol)
    new_str = "".join(list_of_line)

    with open("new_task_10_4.txt", "a") as f:
        f.write(new_str)

