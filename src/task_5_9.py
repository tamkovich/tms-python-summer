m = int(input())
n = int(input())
m, n = min(m, n), max(m, n)
spisok_del = [i + 1 for i in range(n)]
while m <= n:
    pustoi_spis = []
    summa = 0
    for i in spisok_del:
        if m % i == 0 and i < m and i != 1:
            pustoi_spis.append(str(i))
        x = ' '.join(pustoi_spis)
    print(f'{m}: {x}')
    m += 1
