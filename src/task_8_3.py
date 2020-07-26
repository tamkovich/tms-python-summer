from math import sin
def sin1(x: float, e: float) -> float:
    """
    The function calculate sin(x, e)
    :param x: Value in sin(x)
    :param e: Accuracy of calculate
    :return: Result of sin(x, e)
    """
    s = x  # начальное значение функции(нулевой член ряда)
    ch = x  # нулевое значение числителя члена ряда
    zn = 1  # то же знаменателя
    t = ch / zn  # то же самого члена
    i = 1  # первый член
    while abs(t) > e:  # пока очередной больше точности
        ch *= (-1) * x * x  # домножаем числитель на  -x^2
        zn *= 2 * i * (2 * i + 1)  # домножаем знаменатель до очередного факториала
        t = ch / zn  # вычисляем очередной член
        s += t  # считаем сумму
        i += 1  # увеличиваем счетчик
    return s  # значение функции


x = float(input('x = '))
if x != 0:  # проверяем только для x ≠ 0
    for i in range(6):
        eps = float(input('eps = '))
        if eps > 0:
            print(f'Приближенное значение  sin({x})= {sin1(x, eps)}')
            print(f'Аналитическое значение sin({x})= {sin(x)}')
        else:
            print('Ошибка: ε должно быть больше 0!')
else:
    print(' результат: 0')  # ответ при x = 0
