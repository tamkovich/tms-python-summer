# task_9_2
"""Создать lambda функцию, которая принимает на вход неопределенное
количество именных аргументов и выводит словарь с ключами удвоенной
длины. {‘abc’: 5} -> {‘abcabc’: 5}"""

my_func = lambda **kwargs: {key * 2: value for key, value in kwargs.items()}
print(my_func(abc=5, bac=5, cab=5, cba=5))
