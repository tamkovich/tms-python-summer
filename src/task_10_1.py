# Имеется текстовый файл. Напечатать:
# a) его первую строку;
# b) его пятую строку;
# c) его первые 5 строк;
# d) его строки с s1-й по s2-ю;
# e) весь файл.
# Вывел весь фаил
f = open('test1.txt', 'r')
print(f.read())
f.close()
# вывод первой строки
f = open('test1.txt', 'r')
print(f.readline())
f.close()
# вывод 5 строк
f = open('test1.txt', 'r')
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
f.close()
# вывод с 1 по 2 строку
f = open('test1.txt', 'r')
print(f.readline())
print(f.readline())
f.close()
# вывод 5 строки
with open('test1.txt') as f:
  for i, line in enumerate(f):
      if i % 5 == 4:
          print(line)
f.close()