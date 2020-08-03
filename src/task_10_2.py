# Создать текстовый файл и записать в него 6 строк.
# Записываемые строки вводятся с клавиатуры


f = open('../../test.txt', 'w')
n = input()
v = input()
c = input()
x = input()
z = input()
l = input()
for index in [n, v, c, x, z, l]:
    f.write(index + '\n')
f.close()