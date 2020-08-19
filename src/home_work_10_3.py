'''
Задание 10.02
'''

a = input('введите строку 1')
b = input('введите строку 2')
c = input('введите строку 3')
my_file = [a, b, c]
with open("task_10_3.txt", "a") as file:
    for line in my_file:
        file.writelines([line + '\n'])