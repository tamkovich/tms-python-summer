'''
Создать универсальный декоратор, который меняет порядок аргументов в
функции на противоположный.
'''
def universal_decorator(func):
    def universal(*args):
        return func(args [::-1])
    return universal
@universal_decorator
def my_func(*args):
    print(*args)
my_func(1, 2, 3, 4, 5, 6, 7)