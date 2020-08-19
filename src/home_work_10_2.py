'''
Задание 10.02
'''
a = input('введите текст')
b = input('введите текст')
c = input('введите текст')
d = input('введите текст')
e = input('введите текст')
h = input('введите текст')
my_file = [a, b, c, d, e ,h]
with open("task_10_2.txt", "w") as file:
    for  line in my_file:
        file.write(line + '\n')









