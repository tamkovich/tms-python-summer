# Описать функцию Sin1( x , ε ) вещественного типа (параметры x , ε —
# вещественные, ε > 0), находящую приближенное значение функции sin( x ):
# sin( x ) = x – x ^3 /(3!) + x^ 5 /(5!) – ... + (–1) ^ n · x^( 2·n+1) /((2· n +1)!) + ... .
# В сумме учитывать все слагаемые, модуль которых больше ε . С помощью
# Sin1 найти приближенное значение синуса для данного x при шести данных
# ε.

def sin1(x: float, e: float) -> float:
    """
    return sin('x') with precision 'e'
    :param x: float Sin-function argument
    :param e: float precision which sin(x) should be calculated
    :return: float sin(x) with precision e
    """

    def my_factorial(n: int) -> int:
        result = 1
        for i in range(1, n + 1):
            result *= i

        return result

    def member_of_row(x, n):
        if n % 2 == 0:
            flag = 1
        else:
            flag = -1

        return flag * (x ** (2 * n + 1)) / (my_factorial(2 * n + 1))

    n = 0
    sin_x = 0
    tmp_rpw_member = member_of_row(x, n)

    while e < abs(tmp_rpw_member):
        sin_x += tmp_rpw_member
        n += 1
        tmp_rpw_member = member_of_row(x, n)

    return sin_x


print(sin1(3.1415 / 6, 0.00001))
print(sin1(3.1415 / 4, 0.00001))
print(sin1(3.1415 / 3, 0.00001))
print(sin1(3.1415 / 2, 0.00001))
print(sin1(3.1415, 0.00001))
print(sin1(-3.1415 / 2, 0.00001))

print(sin1(-3.1415 / 2, 0.00001))
print(sin1(-3.1415 / 2, 0.0001))
print(sin1(-3.1415 / 2, 0.001))
print(sin1(-3.1415 / 2, 0.01))
print(sin1(-3.1415 / 2, 0.1))
