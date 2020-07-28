import random
e = 0
j = 0
for i in range(0, 19):
    i = random.randint(0, 100)
    if e < i:
        e = i
    if i % 2 == 0:
        i = e
    while j < 19:
        if j % 2 == 0:
            j = e
        j += 1

    print(i)
    i += 1
print(e)

