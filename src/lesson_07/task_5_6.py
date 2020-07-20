# Задан целочисленный массив. Определить количество участков массива,
# на котором элементы монотонно возрастают (каждое следующее число
# больше предыдущего).


def counter(input_list):
    size = len(input_list)
    current = 0
    seq_count = 0

    while current < size:
        i = current
        while i < size - 1 and input_list[i] < input_list[i + 1]:
            i += 1
        else:
            if i > current:
                seq_count += 1
            i += 1
        current = i

    return seq_count


my_list = [1, 2, 3, 2, 3, 4, 1, 2, 9, 8]
print(counter(my_list))

my_list = [4, 4, 3, 2, 3, 4, 1, 2, 9, 10]
print(counter(my_list))
