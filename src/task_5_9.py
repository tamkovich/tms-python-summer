# Для каждого натурального числа в промежутке от m до n вывести все делители,
# кроме единицы и самого числа. m и n вводятся с клавиатуры.
# Пример:m =100, n = 105
m = input("Введите m = ")
n = input("Введите n = ")
d = {}

try:
    m, n, = int(m), int(n)

    for number in range(m, n + 1):
        l = []
        for i in range(2, n + 1):
            if number % i == 0 and i != number:
                l.append(i)
        d[number] = l

    for key, value in d.items():
        print(f"{key}: {value}")
except:
    print("U should enter numbers")