from math import sin, pi, factorial


def sin1(x: float, e: float) -> float:
    """
    The function calculate sin(x, e)
    :param x: Value in sin(x)
    :param e: Accuracy of calculate
    :return: Result of sin(x, e)
    """
    result_sum = x  # начальное значение функции(нулевой член ряда)
    mult_x = x  # нулевое значение числителя члена ряда
    mult_denominator = 1  # то же знаменателя
    term = mult_x / mult_denominator  # то же самого члена
    counter = 1  # первый член
    while abs(term) > e:  # пока очередной больше точности
        mult_x *= -x ** 2  # домножаем числитель на  -x^2
        mult_denominator *= 2 * counter * (2 * counter + 1)  # домножаем знаменатель до очередного факториала
        term = mult_x / mult_denominator  # вычисляем очередной член
        result_sum += term  # считаем сумму
        counter += 1  # увеличиваем счетчик
    return result_sum  # значение функции


while True:
    x = input('x = ')
    if x == 'q':
        break
    try:
        x = float(x)
    except ValueError:
        print('Ошибка ввода')
        continue
    if x != 0:  # проверяем только для x ≠ 0
        for i in range(6):
            try:
                eps = float(input('eps = '))
            except ValueError:
                print('Ошибка ввода')
                break
            if eps > 0:
                print(f'Приближенное значение  sin({x})= {sin1(x, eps)}\n'
                      f'Аналитическое значение sin({x})= {sin(x)}')
            else:
                print('Ошибка: ε должно быть больше 0!')
    else:
        print(' результат: 0')  # ответ при x = 0
