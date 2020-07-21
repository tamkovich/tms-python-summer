import random
num = 19
mas = [random.randint(1, 100) for i in range(num)]
print(mas)
x = max(mas)
dl = len(mas)
kol = 0
print('Самое большое число:', x)
for i in range(dl):
    if mas[i] % 2 == 0:
        mas[i] = x
        kol += 1
print(mas)
print('Произведено замен:', kol)
