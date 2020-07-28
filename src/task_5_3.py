# Два натуральных числа называют дружественными, если каждое из них
# равно сумме всех делителей другого, кроме самого этого числа. Найти все
# пары дружественных чисел, лежащих в диапазоне от 200 до 300. [02-3.2-HL02]
def divisors(number):
    return sum(x for x in range(1, number // 2 + 1) if number % x == 0)
pairs = {}
for i in range(200, 300):
    sum_div = divisors(i)
    if sum_div != 1:
        if i in pairs:
            num1, num2 = i, pairs[i]
            if (num1 // num2) and (divisors(num1) == num2):
                print(*sorted([num2, num1]))
        else:
            pairs[sum_div] = i