# task_10_1
"""Имеется текстовый файл. Напечатать:
a) его первую строку;
b) его пятую строку;
c) его первые 5 строк;
d) его строки с s1-й по s2-ю;
e) весь файл."""

size, list_of_text = 0, []
with open("task_10_1.txt", "r") as f:
    while True:
        line = f.readline()
        if not line:
            break
        size += 1

with open("task_10_1.txt", "r") as f:
    print(f"{f.readline()} - 1st string")

with open("task_10_1.txt", "r") as f:
    list_of_text = f.readlines()
    print(f"\n{list_of_text[4]} - 5th string")

with open("task_10_1.txt", "r") as f:
    print(f"\n{''.join(list_of_text[0:5])} - 1st five string\n")

with open("task_10_1.txt", "r") as f:
    s1 = input("Enter low value: ")
    s2 = input("Enter high value: ")
    print(f"{size} - numbers of strings")

    try:
        s1, s2 = int(s1), int(s2)
    except ValueError:
        print("s1 or s2 not a number")
        exit()

    if s1 < s2 < size:
        print(f"\n{''.join(list_of_text[s1 - 1:s2])} "
              f"- text from {s1} to {s2} strings\n")
    elif s1 < size < s2:
        print(f"\n{''.join(list_of_text[s1 - 1:size])} "
              f"- text from {s1} to {size} strings\n")
    else:
        print("s1 must be less then s2 and"
              " s2 must be less then size")

with open("task_10_1.txt", "r") as f:
    print(f"\n{f.read()} - all text")
