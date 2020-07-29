"""
 Создать универсальный декоратор,
  который меняет порядок аргументов в функции на противоположный
"""
def unidec(functionn):
    def reversoder(x):
        return x[::-1]
    return  reversoder
@unidec
def back(a):
    spis = [i**2 for i in a]
    return spis
c = [1, 3, 5, 4]
print(back(c))
