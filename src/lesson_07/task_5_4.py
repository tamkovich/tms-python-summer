# Для заданного числа N составьте программу вычисления суммы
# S=1+1/2+1/3+1/4+...+1/N, где N – натуральное число.


def harmonic_row_sum(n: int) -> float:
    """
    finds sum of harmonic row to 'n'-member
    :param n: number of member sequences
    :return s: sum of all members to 'n'-member
    """
    s = 0
    for i in range(1, n + 1):
        s += 1 / i
    return s


print(harmonic_row_sum(3))
