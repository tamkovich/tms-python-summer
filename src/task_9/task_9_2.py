"""
Создать lambda функцию, которая принимает на вход неопределенное
количество именных аргументов и выводит словарь с ключами удвоенной
длины. {‘abc’: 5} -> {‘abcabc’: 5}
"""


f = lambda **kwargs: {key * 2: value for key, value in kwargs.items()}
print(f(a=1, ww=2, thr=3, four=4, fives=5))
