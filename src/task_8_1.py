# Описать функцию fact2( n ), вычисляющую двойной факториал :n!! =
# 1·3·5·...·n, если n — нечетное; n!! = 2·4·6·...·n, если n — четное (n > 0 —
# параметр целого типа. С помощью этой функции найти двойные
# факториалы пяти данных целых чисел [01-11.2-Proc35]



def func2(n: int) -> int:
    res = 1
    if n % 2 == 0:
        for i in range(2, n, 2):
            res *= i
    else:
        for i in range(1, n, 2):
            res *= i
    return res
print(func2(15))

