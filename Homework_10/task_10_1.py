my_file = open('test.txt', 'r')
while True:
    for i in range(10):
        line = my_file.readline()
        if i == 0:  # Выводит первую строку(10_1 задание a)
            print(line)
        elif i == 4:  # Выводит пятую строку(10_1 задание b)
            print(line)
    if not line:
        break
my_file.close()

my_file = open('test.txt', 'r')
for i in range(5):
    line = my_file.readline()  # Выводит первые 5 строк(10_1 задание c)
    print(line)
my_file.close()

my_file = open('test.txt', 'r')
s1 = int(input('s1: '))
s2 = int(input('s2: '))
while s1 < s2 + 1:  # Выводит строки от s1 до s2(10_1 задание d)
    line = my_file.readline()
    print(line)
    s1 += 1
my_file.close()

my_file = open('test.txt', 'r')
while True:  # Выводит все строки(10_1 задание e)
    line = my_file.readline()
    if not line:
        break
    print(line)
my_file.close()
