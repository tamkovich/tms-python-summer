# task_9_4
"""Создать универсальный декоратор, который меняет порядок аргументов в
функции на противоположный."""


def universal_dec(func):
    def reverse(*args: list) -> func or str:
        """
        Return reverse list, if it consists only from numbers;
        Return message, if elements from list not int or float
        :param args: list with numbers
        :return: reverse list
        """
        try:
            return func(*args[::-1])
        except TypeError:
            return "Error"

    return reverse


@universal_dec
def my_func(*args: list):
    """
    Print reverse list
    :param args: reverse list with numbers
    :return: nothing
    """
    print(args)


a, b, = 3, 4
my_func(a, b)
