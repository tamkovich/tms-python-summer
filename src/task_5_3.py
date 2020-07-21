nachalo = 200
konec = 300
spis_elem = [(nachalo-1) + 1 for nachalo in range(nachalo, konec + 1)]
spisok_del = [i + 1 for i in range(konec)]
pust_spis_summ_del = []
while nachalo <= konec:
    pustoi_spis = []
    summa = 0
    for i in spisok_del:
        if nachalo % i == 0 and i < nachalo:
            pustoi_spis.append(i)
            summa += i
    pust_spis_summ_del.append(summa)
    nachalo += 1
slov = dict(zip(spis_elem, pust_spis_summ_del))
nachalo = 200
konec = 300
while nachalo <= konec:
    summa = 0
    x = slov[nachalo]
    for i in spisok_del:
        if x % i == 0 and i < x:
            summa += i
    if summa == nachalo:
        print(f'{summa} и {x} - пара дружественных чисел')
    nachalo += 1
