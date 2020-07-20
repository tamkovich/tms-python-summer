# Для каждого натурального числа в промежутке от m до n вывести все делители,
# кроме единицы и самого числа. m и n вводятся с клавиатуры.
# Пример:m =100, n = 105
# 100: 2 4 5 10 20 25 50
# 101:
# 102: 2 3 6 17 34 51
# 103:
# 104: 2 4 8 13 26 52
# 105: 3 5 7 15 21 35
a = []
dict_a = {}
for i in range(int(input("M: ")), int(input("N: ")) + 1):
    b = []
    dict_b = {}
    c = []
    for f in range(2, i):
        if i % f == 0:
            b.append(f)
            dict_b.update({i: b})
        else:
            dict_b.update({i: b})

    a.append(b)
    dict_a.update(dict_b)
for key in dict_a.keys():
    print(f"{key}: ", end=" ")
    for value in dict_a[key]:
        print(f"{value}", end=" ")
    print()
