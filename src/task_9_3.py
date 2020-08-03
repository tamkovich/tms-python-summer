# Создать декоратор для функции, которая принимает список чисел.
# Декоратор должен производить предварительную проверку данных -
# удалять все четные элементы из списка.

my_list = [1, 2, 3, 4, 5, 6, 7, 8]


def my_decorator(func):
    def delete_odd_elem(*args):
        return func([i for i in args[0] if i % 2 != 0])

    return delete_odd_elem


@my_decorator
def my_func(numbers: list):
    print(numbers)


my_func(my_list)
