e = 0
c = 0
d= 0
a = []
for chi in range(200, 300):
    b = []
    for i in range(1, chi):
        if chi % i == 0:
            e += i
            b.append(e)
            e -= i

        i += 1
    a.append(b)

    # print(chi, c)
    chi += 1
h = []

for b in a:
    d = 0
    for elem in b:
        d += elem
    h.append(d)

print(h)


sp = []
for qq in range(200, 300):
    sp.append(qq)
print(sp)
sl = dict(zip(sp, h))
print(sl)

ez = 0
for chi in range(200, 300):
    for i in range(1, chi):
        if chi % i == 0:
            ez += i
qw = []
print(ez)
for ii, u in range(200, 300):
    if ez % sl[ii] == 0  and ez % sl[u] == 0 and u != ii and sl[ii] == sl[u]:
        qw.append(sl)
print(qw) #Почему-то не запускается, хотя врооде сделал все правильно.
