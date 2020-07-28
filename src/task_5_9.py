#Для каждого натурального числа в промежутке от m до n вывести все делители,
#кроме единицы и самого числа. m и n вводятся с клавиатуры.

a = input("Введите число начала = ")
b = input("Введите число конца = ")
d = {}

try:
    a, b, = int(a), int(b)

    for number in range(a, b + 1):
        l = []
        for i in range(2, b + 1):
            if number % i == 0 and i != number:
                l.append(i)
        d[number] = l

    for key, value in d.items():
        print(f"{key}: {value}")
except:
    print("Не коректный ввод!")
