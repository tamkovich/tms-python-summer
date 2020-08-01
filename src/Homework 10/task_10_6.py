# task_10_6
"""Имеются два текстовых файла с одинаковым числом
строк. Выяснить, совпадают ли их строки. Если нет, то
получить номер первой строки, в которой эти файлы
отличаются друг от друга."""

check, tmp = True, 0
with open("task_10_6_1.txt", "r") as f:
    text1 = f.readlines()

with open("task_10_6_2.txt", "r") as f:
    text2 = f.readlines()

if len(text1) == len(text2):
    length = len(text1)
    for i in range(length):
        if text1[i] != text2[i]:
            check = False
            tmp = i
            break

    if check:
        print("The files are the same")
    else:
        print("The files are not the same")
        print(f"They differ in {tmp} line")
else:
    print("Files have the different sizes")
