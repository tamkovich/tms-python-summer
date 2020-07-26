from random import randint


def fact2(n):
    result = 1
    if n % 2 != 0:
        for i in range(1, n + 1, 2):
            result *= i
        print(result)
    else:
        for i in range(2, n + 1, 2):
            result *= i
        print(result)
    return result


random_numbs = [randint(1, 10) for i in range(5)]
print(random_numbs)
for i in random_numbs:
    fact2(i)
