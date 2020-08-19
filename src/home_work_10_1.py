'''
Задание 10.01
'''
with open('test_my.txt') as f:
    lines = f.readlines()
print(lines[0]) # вывод 1-ой строки
print(lines[4]) # вывод 5-ой строки
for i in range(0, 5):
    print(lines[i]) # вывод первых 5-ти строк
for j in range(0, 2):
    print(lines[j]) # вывод первых 2-х строк
f = open('test_my.txt', 'r')
print(f.read()) # вывод всех строк
f.close()