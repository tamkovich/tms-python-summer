# task_10_2
"""Создать текстовый файл и записать в него 6 строк.
Записываемые строки вводятся с клавиатуры."""

with open("task_10_2.txt", "w") as f:
    for i in range(6):
        text = input("Enter something: ")
        f.write(f"{text}\n")
