"""
Описать функцию Sin1( x , ε ) вещественного типа (параметры x , ε —
вещественные, ε > 0), находящую приближенное значение функции sin( x ):
sin( x ) = x – x ^3 /(3!) + x^ 5 /(5!) – ... + (–1) ^ n · x^( 2·n+1) /((2· n +1)!) + ... .
В сумме учитывать все слагаемые, модуль которых больше ε . С помощью
Sin1 найти приближенное значение синуса для данного x при шести данных
ε.
"""
import math
def sin(x: float, e: int) -> float:
    """
    Функция по расчету синуса.
    :param x: float
    :param e > 0: int
    :return: float
    """

    if e < 1:
        print("Error! e must be > 0")
    else:
        result = 0
        for i in range(1, e+1):
            result += ((-1)**i * x**(2*i + 1))/math.factorial(2*i+1)
        return result

print(sin(1.5, 6))