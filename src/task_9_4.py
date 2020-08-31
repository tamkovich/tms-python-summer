# Создать универсальный декоратор, который меняет порядок аргументов в
# функции на противоположный.

my_list = [1, 2, 3, 4, 5 ,6 ,7 ,8]


def my_decorator_universal(func):
    def xz_universal(*args):
        return func(my_list[::-1])
    return xz_universal

@my_decorator_universal
def my_func(numbers: list):
    print(numbers)


my_func(my_list)