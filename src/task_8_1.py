"""Описать функцию fact2( n ), вычисляющую двойной факториал :n!! =
1·3·5·...·n, если n — нечетное; n!! = 2·4·6·...·n, если n — четное (n > 0 —
параметр целого типа. С помощью этой функции найти двойные
факториалы пяти данных целых чисел"""

def fact2(n: int) -> int:
    if n <= 0:
        return 1
    else:
        return fact2(n - 2) * n

while True:
    number = input("Введите число (для выхода введите -1): ")

    if number == "-1":
        exit()
    try:
        number = int(number)
    except TypeError:
        print("Некоректный ввод")

    print(f"Число: {number}\n{number}!! = {fact2(number)}")
