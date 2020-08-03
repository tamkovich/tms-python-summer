# task_9_3
"""Создать декоратор для функции, которая принимает список чисел.
Декоратор должен производить предварительную проверку данных -
удалять все четные элементы из списка."""


def decorator_delete(func):
    def delete_even_element(*args: list) -> list:
        """
        Return list with uneven numbers
        :param args: list with numbers
        :return: new list with required numbers
        """
        return func([i for i in args[0] if i % 2 != 0])

    return delete_even_element


@decorator_delete
def my_func(numbers: list) -> list or str:
    """
    Checking numbers from a list for their type
    :param numbers: list of numbers
    :return: list with uneven numbers or message
    """
    try:
        return numbers
    except TypeError:
        return "numbers not a numbers"


list_of_numbers = [i for i in range(0, 20)]
print(my_func(list_of_numbers))
