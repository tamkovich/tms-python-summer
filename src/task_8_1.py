from random import randint


def fact2(n: list) -> list:
    """
    двойной факториал :
    n!! = 1·3·5·...·n, если n — нечетное;
    n!! = 2·4·6·...·n, если n — четное
    (n > 0) — параметр целого типа
    :param n: n > 0
    :return: list with double factorial
    """
    result_sum = []
    for g in n:
        result = 1
        if g % 2 != 0:
            for i in range(1, g + 1, 2):
                result *= i
        else:
            for i in range(2, g + 1, 2):
                result *= i
        result_sum.append(result)
    return result_sum


random_numbs = [randint(1, 10) for i in range(5)]
print(f'Исходный лист: {random_numbs}\n'
      f'Факториал листа: {fact2(random_numbs)}')
