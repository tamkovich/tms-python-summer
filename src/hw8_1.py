def factorial(n: int) -> int:

    pr = 1
    if n % 2 != 0:
        for i in range(1, n + 1, 2):
            pr *= i

    elif n % 2 ==0:
        for i in range(2, n + 1, 2):
            pr *= i
    return pr
n = [13, 56, 42, 18, 21]
for i in n:
    print(f'{i} = {factorial(i)}')


