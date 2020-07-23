"""
Для каждого натурального числа в промежутке от m до n вывести все делители,
кроме единицы и самого числа. m и n вводятся с клавиатуры.
Пример:m =100, n = 105
100: 2 4 5 10 20 25 50
101:
102: 2 3 6 17 34 51
103:
104: 2 4 8 13 26 52
105: 3 5 7 15 21 35
"""

"""Ввести два натуральных числа, отличных от единицы и нуля"""
try:
    m = abs(int(input('Enter some number:')))
    n = abs(int(input('Enter some number')))
except ValueError:
    print("m and m must be intenger")
m = min(m, n)

for num in range(m, n + 1):
    divisions = []  # доступные делители будут собираться в этот список
    dict_divisions = {}

    for div in range(2, int(num/2)):
        if num % div == 0:
            divisions.append(div)
            dict_divisions.update({num: divisions})
        else:
            dict_divisions.update({num: divisions})

    for key in dict_divisions.keys():
        print(f'{key}: ', end=" ")

        for value in dict_divisions[key]:
            print(f'{value}', end=" ")
    print()
