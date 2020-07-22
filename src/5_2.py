# task_5_2
# Дано число. Найти сумму и произведение его цифр.

number = input("Enter a number: ")
length = len(number)
summa, mult, tmp = 0, 1, 1

try:
    number = int(number)
    while length > 0:
        summa += number // tmp % 10
        mult *= number // tmp % 10
        tmp *= 10
        length -= 1
    print(f"Summa: {summa}")
    print(f"Mult: {mult}")

except TypeError:
    print("U should enter a number")
