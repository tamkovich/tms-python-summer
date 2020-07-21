import random
num = int(input())
mas = [random.randint(1, 30) for i in range(num)]
print(mas)
size = len(mas)
count = 0
bool_F_T = False
i = 1
while i < size:
    if mas[i] > mas[i-1]:
        bool_F_T = True
    elif bool_F_T:
        count += 1
        bool_F_T = False
    i += 1
if bool_F_T:
    count += 1
print(count)
