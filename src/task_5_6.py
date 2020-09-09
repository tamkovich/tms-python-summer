a = [12, 324, 24, 24 ,235, 325, 43, 5,53, 2, 234, 43, 423, 3424, 4]
b = len(a)
i = 0
c = 0
for i in range(b -1):
    if a[i] <a[i+1] and a[i +1] >= a[i +2]:
        c +=1
print(c)
