# В массиве целых чисел с количеством элементов 19 определить максимальное
# число и заменить им все четные по значению элементы.


def task(input_list):
    """
    finds max element in 'input_list' and replaces them all odd elements
    :param input_list: input list
    """
    max_val = max(input_list)

    for i in range(len(input_list)):
        if input_list[i] % 2 == 0:
            input_list[i] = max_val


import random

my_list = []
for i in range(19):
    my_list.append(random.randint(0, 100))

print(my_list)
task(my_list)
print(my_list)
