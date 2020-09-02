# Создать универсальный декоратор, который меняет порядок аргументов в
# функции на противоположный.

def inverse_decorator(func):
    def invert(*args):
        return func(args[::-1])

    return invert


@inverse_decorator
def test_func(*args):
    print(args)


a = 5
b = 4
c = 'str'

test_func(a, b)
