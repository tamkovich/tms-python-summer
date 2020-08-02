"""
Создать универсальный декоратор, который меняет порядок аргументов в
функции на противоположный.
"""

def decor_arg_revers(func):
    """
    декоратор функции.
    меняет порядок аргументов на проивоположный
    :param func: функция с любым количеством аргументов
    :return: функция с обратным порядком аргументов
    """
    def revers(*args):
        revers_args = args[::-1]
        try:
            return(func(*revers_args))
        except TypeError:
            return "Error arguments type"
    return revers

@decor_arg_revers
def f_sqw(a: int, b: int, c: int) -> str:
    """
    функция для решения квадратных уравнений
    :param a: int
    :param b: int
    :param c: int
    :return result: str(результат одной строкой)
    """

    D = b ** 2 - 4 * a * c
    if D > 0:
        x_1 = (-b + D ** .5)/(2*a)
        x_2 = (-b - D ** .5)/(2*a)
        result = (x_1, x_2)
    elif D == 0:
        x = -b/(2*a)
        result = x
    else:
        result = None
    return result

print(f_sqw(10, 20, 6))
print(f_sqw(6, 20, 10))  # для проверки без декоратора
