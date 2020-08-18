# task_8_1
"""Описать функцию fact2( n ), вычисляющую двойной факториал :n!! =
1·3·5·...·n, если n — нечетное; n!! = 2·4·6·...·n, если n — четное (n > 0 —
параметр целого типа. С помощью этой функции найти двойные
факториалы пяти данных целых чисел"""


def fact2(n: int) -> int:
    """
    The function calculate double factorial
    :param n: from n will calculate double factorial
    :return: double factorial from number
    """
    return fact2(n - 2) * n if n > 0 else 1


while True:
    number = input("Enter a number (if u want exit, input -1): ")

    if number == "-1":
        exit()

    try:
        number = int(number)
    except TypeError:
        print("Not a number")
        continue

    print(f"Number: {number}\n{number}!! = {fact2(number)}")
