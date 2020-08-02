"""
Имеются два текстовых файла с одинаковым числом
строк. Выяснить, совпадают ли их строки. Если нет, то
получить номер первой строки, в которой эти файлы
отличаются друг от друга.
"""


f1 = open('t1.txt', 'r')
f2 = open('t2.txt', 'r')
line1 = f1.readlines()
line2 = f2.readlines()
i = 0
while i < len(line1):
    i += 1
    if line1[i] == line2[i]:
        pass
    else:
        print(i)
        break
f1.close()
f2.close()