# Создать универсальный декоратор, который меняет порядок аргументов в
# функции на противоположный.

from typing import Any


def arg_reverse(func):
    def input_args(*args):
        return func(*list(args)[::-1])

    return input_args


@arg_reverse
def test(a: Any, b: Any) -> tuple:
    return a, b


print(test([232], 3213))
