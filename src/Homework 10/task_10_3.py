# task_10_3
"""В конец существующего текстового файла записать три новые
строки текста. Записываемые строки вводятся с клавиатуры."""

with open("task_10_3.txt", "a") as f:
    for i in range(3):
        text = input("Enter something: ")
        f.write(f"\n{text}")