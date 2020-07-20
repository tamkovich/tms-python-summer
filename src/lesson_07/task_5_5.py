# В массиве целых чисел с количеством элементов 19 определить максимальное
# число и заменить им все четные по значению элементы.


def task(input_list):
    max = input_list[0]
    for i in range(len(input_list)):
        if max < input_list[i]:
            max = input_list[i]

    for i in range(len(input_list)):
        if input_list[i] % 2 == 0:
            input_list[i] = max


import random

my_list = []
for i in range(19):
    my_list.append(random.randint(0, 100))

print(my_list)
task(my_list)
print(my_list)
