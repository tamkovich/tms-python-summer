# task_8_3
"""Описать функцию Sin1( x , ε ) вещественного типа (параметры x , ε —
вещественные, ε > 0), находящую приближенное значение функции sin( x ):
sin(x) = x – x^3 / (3!) + x^5 / (5!) – ... + (–1)^n · x^(2·n+1) / ((2· n +1)!).
В сумме учитывать все слагаемые, модуль которых больше ε . С помощью
Sin1 найти приближенное значение синуса для данного x при шести данных"""

import math


def sin1(x: float, e: float) -> float:
    """
    The function calculate sin(x)
    :param x: Value in sin(x)
    :param e: Accuracy of calculate
    :return: Result of sin(x)
    """
    n, res = 0, 0
    while True:
        power = 2 * n + 1
        tmp = x ** power / math.factorial(power)
        res += (-1) ** n * tmp
        n += 1
        if abs(tmp) < e:
            return res


exp = input("Enter accuracy: ")
while True:
    number = input("Enter a number (if u want exit, input exit): ")

    if number.lower() == "exit":
        exit()

    try:
        exp, number = float(exp), float(number)
    except TypeError:
        print("Not a number")
        continue

    print(f"sin({number}) = {sin1(number, exp)}")
