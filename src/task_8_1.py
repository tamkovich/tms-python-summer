# Описать функцию fact2( n ), вычисляющую двойной факториал :n!! =
# 1·3·5·...·n, если n — нечетное; n!! = 2·4·6·...·n, если n — четное (n > 0 —
# параметр целого типа. С помощью этой функции найти двойные
# факториалы пяти данных целых чисел.

def fact2(n: int) -> int:
    """
    return factorial (2 * 4 * ... * n) if n - even, and (1 * 3 * ... * n) if n - odd;
    if n <= 0 or not integer - return -1
    :param n: integer > 0
    :return result: integer
    """

    if n <= 0 or type(n) is not int:
        return -1

    if n % 2 == 0:
        result = 2
        while n > 2:
            result *= n
            n -= 2
    else:
        result = 1
        while n > 1:
            result *= n
            n -= 2

    return result


# testing
# even numbers
if 8 != fact2(4):
    print(f'error, fact2(4) = {fact2(4)}')
else:
    print(f'test has passed, fact2(4) = {fact2(4)}')

if 48 != fact2(6):
    print(f'error, fact2(6) = {fact2(6)}')
else:
    print(f'test has passed, fact2(6) = {fact2(6)}')

if 2 != fact2(2):
    print(f'error, fact2(2) = {fact2(2)}')
else:
    print(f'test has passed, fact2(2) = {fact2(2)}')

# odd numbers
if 3 != fact2(3):
    print(f'error, fact2(3) = {fact2(3)}')
else:
    print(f'test has passed, fact2(3) = {fact2(3)}')

if 15 != fact2(5):
    print(f'error, fact2(5) = {fact2(5)}')
else:
    print(f'test has passed, fact2(5) = {fact2(5)}')

if 105 != fact2(7):
    print(f'error, fact2(7) = {fact2(7)}')
else:
    print(f'test has passed, fact2(7) = {fact2(7)}')

# n <= 0 and not integer
if -1!= fact2(0):
    print(f'error, fact2(0) = {fact2(0)}')
else:
    print(f'test has passed, fact2(0) = {fact2(0)}')

if -1 != fact2(-7):
    print(f'error, fact2(-7) = {fact2(-7)}')
else:
    print(f'test has passed, fact2(-7) = {fact2(-7)}')

print(f'34!! = {fact2(34)}')
print(f'12!! = {fact2(12)}')
print(f'23!! = {fact2(23)}')
print(f'9!! = {fact2(9)}')
print(f'51!! = {fact2(51)}')
