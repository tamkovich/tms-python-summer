import random
n = int(input())
l = []
for i in range(n):
    vloz_spis = []
    for j in range(n):
        j = random.randint(1, 50)
        vloz_spis.append(j)
        print(j, end=' ')
    print()

    x = max(vloz_spis)
    y = vloz_spis[i]
    indeks = vloz_spis.index(x)

    del vloz_spis[i]
    vloz_spis.insert(i, x)

    del vloz_spis[indeks]
    vloz_spis.insert(indeks, y)

    l.append(vloz_spis)
print('--------------------------')
for i in l:
    print(i)
