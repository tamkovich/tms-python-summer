"""
Описать функцию fact2( n ), вычисляющую двойной факториал :n!! =
1·3·5·...·n, если n — нечетное; n!! = 2·4·6·...·n, если n — четное (n > 0 —
параметр целого типа. С помощью этой функции найти двойные
факториалы пяти данных целых чисел
"""


def fact_2(n: int) -> int:
    """
    Функция по вычислению двойного факториала (n!!)
    на вход принимает целое число, больше нуля
    на выходе результат - двойной факториал заданного числа n
    :param n: int > 0
    :return: int
    """

    count = 1
    if n % 2 != 0:
        for i in range(1, n+1, 2):
            count *= i
    elif n % 2 == 0:
        for i in range(2, n+1, 2):
            count *= i

    return count


n = [5, 10, 21, 28, 55]
for i in n:
    print(f'{i}!! = {fact_2(i)}')
