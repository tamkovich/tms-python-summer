"""
Описать функцию fact2( n ),
 вычисляющую двойной факториал :n!! = 1·3·5·...·n, если n — нечетное;
 n!! = 2·4·6·...·n, если n — четное (n > 0 — параметр целого типа.
 С помощью этой функции найти двойные факториалы пяти данных целых чисел
"""
def fact2(n):
    counter_odd = 1
    counter_even = 1
    if n > 0:
        if n % 2 == 0:
            for i in range(2, n+1, 2):
                counter_even *= i
            return counter_even
        else:
            for j in range(1, n+1, 2):
                counter_odd *= j
            return counter_odd
    else:
        print('number must be positiv')
n = 41
b = 12
e = 24
g = 15
m = 7
print(fact2(n))
print(fact2(b))
print(fact2(e))
print(fact2(g))
print(fact2(m))



