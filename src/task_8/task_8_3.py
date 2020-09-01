"""
Описать функцию Sin1( x , ε ) вещественного типа (параметры x , ε —
вещественные, ε > 0), находящую приближенное значение функции sin( x ):
sin( x ) = x – x ^3 /(3!) + x^ 5 /(5!) – ... + (–1) ^ n · x^( 2·n+1) /((2· n +1)!) + ... .
В сумме учитывать все слагаемые, модуль которых больше ε . С помощью
Sin1 найти приближенное значение синуса для данного x при шести данных
ε.
"""
import math
def sin1(x: float, e: float) -> float:
    """
    Функция по расчету синуса угла в радианах.
    :param x: float. значение, по которому вычисляется синус (в радианах)
    :param e > 0: float. точность, с которой высчитыввется приближенное значение синуса)
    :return: float. возвращает значение синуса в радианах, от заданного x с точностью e.
    """

    result = 0
    n = 0
    while True:
        tmp = ((-1)**n * x**(2*n + 1))/math.factorial(2*n+1)
        result += tmp
        n += 1
        if abs(tmp) <= abs(e):
            break
    return result

try:
    x = float(input(":"))
except ValueError:
    print("x is no digit!")
try:
    lis = [0.5, 0.1, 0.01, 0.001, 0.0001, 0.00001]
    for i in lis:
        print(f'sin от {x} = {sin1(x, i)} при точности {i}')
except:
    print("Please enter x - digit")
