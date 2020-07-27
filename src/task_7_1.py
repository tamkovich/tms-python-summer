# Написать 12 функций по переводу:
# 1. Дюймы в сантиметры
# 2. Сантиметры в дюймы
# 3. Мили в километры
# 4. Километры в мили
# 5. Фунты в килограммы
# 6. Килограммы в фунты
# 7. Унции в граммы
# 8. Граммы в унции
# 9. Галлон в литры
# 10. Литры в галлоны
# 11. Пинты в литры
# 12. Литры в пинты
# Примечание: функция принимает на вход число и возвращает конвертированное число
# 2. Написать программу, со следующим интерфейсом: пользователю предоставляется на
# выбор 12 вариантов перевода(описанных в первой задаче). Пользователь вводит цифру
# от одного до двенадцати. После программа запрашивает ввести численное значение.
# Затем программа выдает конвертированный результат. Использовать функции из первого
# задания. Программа должна быть в бесконечном цикле. Код выхода из программы - “0”

def perevodchik1 (n, m):
    inch = 2.54
    if m == 'duim':
        print('{} inch = {} cm'. format(n,(n*inch)))
perevodchik1 (int(input()), 'duim')

def perevodchik2 (n, m):
    inch = 2.54
    if m == 'cm':
        print("{} cm = {} inch ".format(n, (round(n / inch, 2))))
perevodchik2 (int(input()), 'cm')

def perevodchik3 (n, m):
    km = 1.61
    if m == 'km':
        print('{} mila = {} km'. format(n,(n*km)))
perevodchik3 (int(input()), 'km')

def perevodchik4 (n, m):
    km = 1.61
    if m == 'mila':
        print("{} km = {} mila ".format(n, (round(n / km, 2))))
perevodchik4 (int(input()), 'mila')


def perevodchik5 (n, m):
    kilo = 0.45
    if m == 'kilo':
        print('{} funt = {} kilo'. format(n,(n*kilo)))
perevodchik5 (int(input()), 'kilo')

def perevodchik6 (n, m):
    kilo = 0.45
    if m == 'funt':
        print("{} kilo = {} funt ".format(n, (round(n / kilo, 2))))
perevodchik6 (int(input()), 'funt')

def perevodchik7 (n, m):
    unzia = 0.035
    if m == 'unzia':
        print('{} gramm = {} unzia'. format(n,(n*unzia)))
perevodchik7 (int(input()), 'unzia')

def perevodchik8 (n, m):
    unzia = 0.035
    if m == 'gramm':
        print("{} unzia = {} gramm ".format(n, (round(n / unzia, 2))))
perevodchik8 (int(input()), 'gramm')

def perevodchik9 (n, m):
    litr = 3.785
    if m == 'litr':
        print('{} gallon = {} litr'. format(n,(n*litr)))
perevodchik9 (int(input()), 'litr')

def perevodchik10 (n, m):
    litr = 3.785
    if m == 'gallon':
        print("{} litr = {} gallon ".format(n, (round(n / litr, 2))))
perevodchik10 (int(input()), 'gallon')

def perevodchik11 (n, m):
    pinta = 2.113
    if m == 'pinta':
        print('{} litr = {} pinta'. format(n,(n*pinta)))
perevodchik11 (int(input()), 'pinta')

def perevodchik12 (n, m):
    pinta = 2.113
    if m == 'litr':
        print("{} pinta = {} litr ".format(n, (round(n / pinta, 2))))
perevodchik12 (int(input()), 'litr')
