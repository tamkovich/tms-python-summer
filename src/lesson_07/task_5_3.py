# Два натуральных числа называют дружественными, если каждое из них
# равно сумме всех делителей другого, кроме самого этого числа. Найти все
# пары дружественных чисел, лежащих в диапазоне от 200 до 300.

def find_sum_divisors(x: int) -> int:
    result_sum = 0
    y = 1
    while y <= x ** 0.5:
        if x % y == 0:
            result_sum += y + int(x / y)
        y += 1
    return result_sum


def find_couple(left: int, right: int) -> list:
    """
    :param left: min value of finding range
    :param right: max value of finding range
    :return: list of amicable numbers in finding range
    """
    couples = []

    for i in range(left, right + 1):
        n1 = find_sum_divisors(i) - i
        if n1 > i and i == find_sum_divisors(n1) - n1:
            couples.append(str(i) + ' - ' + str(n1))

    return couples


couplea = find_couple(0, 10000)
print(couplea)
