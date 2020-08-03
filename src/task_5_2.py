# Дано число. Найти сумму и произведение его цифр.

n = int(input())

suma = 0
mult = 1

while n > 0:
    digit = n % 10
    if digit != 0:
        suma += digit
        mult *= digit
    n = n // 10

print("Сумма:", suma)
print("Произведение:", mult)