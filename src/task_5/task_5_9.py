"""Ввести два натуральных числа, отличных от единицы и нуля"""
m = abs(int(input('Enter some number:')))
n = abs(int(input('Enter some number')))
m = min(m, n)

for num in range(m, n + 1):
    divisions = []  # доступные делители будут собираться в этот список
    dict_divisions = {}

    for div in range(2, num - 1):
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
