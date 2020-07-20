# 3) Два натуральных числа называют дружественными, если каждое из них
# равно сумме всех делителей другого, кроме самого этого числа. Найти все
# пары дружественных чисел, лежащих в диапазоне от 200 до 300. [02-3.2-HL02]
a = 200 
b = 300
spis_elem = [(a - 1) + 1 for a in range(a, b + 1)]
spisok_del = [i + 1 for i in range(b)]
pust_spis_summ_del = []
while a <= b:
    pustoi_spis = []
    summa = 0
    for i in spisok_del:
        if a % i == 0 and i < a:
            pustoi_spis.append(i)
            summa += i
    pust_spis_summ_del.append(summa)
    a += 1
slov = dict(zip(spis_elem, pust_spis_summ_del))
a = 200
b = 300
while a <= b:
    summa = 0
    x = slov[a]
    for i in spisok_del:
        if x % i == 0 and i < x:
            summa += i
    if summa == a:
        print(f'{summa} и {x} - пара дружественных чисел')
    a += 1
