"""
Создать декоратор для функции, которая принимает список чисел.
 Декоратор должен производить предварительную проверку данных -
 удалять все четные элементы из списка
"""
def decor(funct):
    def evenel(x):
        l = [i for i in x if i % 2 == 0]
        return l
    return evenel
@decor
def returner(a):
    return a
li = [23, 28, 54, 23, 54, 66, 43, 54]
print(returner(li))



