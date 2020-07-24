# Два натуральных числа называют дружественными, если каждое из них
# равно сумме всех делителей другого, кроме самого этого числа. Найти все
# пары дружественных чисел, лежащих в диапазоне от 200 до 300.

dict_a = {}
for i in range(200, 300):
    dict_b = {}
    c = 0
    for f in range(1, int(i/2) + 1):
        if i % f == 0:
            c += f
            dict_b.update({i: c})
    dict_a.update(dict_b)

for key in dict_a.keys():
    for key1 in dict_a.keys():
        if key == dict_a[key1] and dict_a[key] == key1:
            print(key)
