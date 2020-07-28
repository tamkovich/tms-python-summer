"""
Описать функцию Sin1( x , ε ) вещественного типа (параметры x , ε —
вещественные, ε > 0), находящую приближенное значение функции sin( x ):
sin( x ) = x – x ^3 /(3!) + x^ 5 /(5!) – ... + (–1) ^ n · x^( 2·n+1) /((2· n +1)!) + ... .
В сумме учитывать все слагаемые, модуль которых больше ε . С помощью
Sin1 найти приближенное значение синуса для данного x при шести данных
ε.
"""

import math
def sin1(x: float, e: int) -> float:
    """
    Функция по расчету синуса.
    :param x: float
    :param e > 0: float
    :return: float
    """

    if e <= 0:
        print("Error! e must be > 0")
    else:
        result = 0
        n = 0
        while True:
            tmp = ((-1)**n * x**(2*n + 1))/math.factorial(2*n+1)
            result += tmp
            n += 1
            if abs(tmp) <= e:
                break
    return result

x = float(input("Enter value:"))
lis = [0.5, 0.1, 0.01, 0.001, 0.0001, 0.00001]
for i in lis:
    print(f'sin от {x} = {sin1(x, i)} при точности {i}')
