
import random
a=[]
for i in range(1,6):
    b = []
    for j in range(1,6):
        b.append(random.randint(0,99))
    a.append(b)
print(a)
f = []
u = 0
m = b[0]
q = len(b)
for b in a:
    for e in range(q):
        if u % 5 == 0:
            m = 0
        u += 1
        if b[e] > m:
            m = b[e]
    f.append(m)
print(f)
x = 0
for b in a:
    temp = b[x]
    b[x] = f[x]
    f[x] = temp
    x += 1
print(a)
print(f)