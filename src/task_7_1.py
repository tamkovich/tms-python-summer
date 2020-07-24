# 1. Написать 12 функций по переводу:
#     1. Дюймы в сантиметры
#     2. Сантиметры в дюймы
#     3. Мили в километры
#     4. Километры в мили
#     5. Фунты в килограммы
#     6. Килограммы в фунты
#     7. Унции в граммы
#     8. Граммы в унции
#     9. Галлон в литры
#     10. Литры в галлоны
#     11. Пинты в литры
#     12. Литры в пинты
# Примечание: функция принимает на вход число и возвращает конвертированное число
# 2. Написать программу, со следующим интерфейсом: пользователю предоставляется на
#     выбор 12 вариантов перевода(описанных в первой задаче). Пользователь вводит цифру
#     от одного до двенадцати. После программа запрашивает ввести численное значение.
#     Затем программа выдает конвертированный результат. Использовать функции из первого
#     задания. Программа должна быть в бесконечном цикле. Код выхода из программы - “0”.

# 1. Дюймы в сантиметры
def inch_to_sm(a):
    if not type(a) == int and not type(a) == float:
        print("input only digit!")
    elif a == 0:
        print('value is zero')
    else:
        result = a / 0.39
        return result


# 2. Сантиметры в дюймы
def sm_to_inch(a):
    if not type(a) == int and not type(a) == float:
        print("input only digit!")
    elif a == 0:
        print('value is zero')
    else:
        result = a * 0.39
        return result


# 3. Мили в километры
def mile_to_km(a):
    if not type(a) == int and not type(a) == float:
        print("input only digit!")
    elif a == 0:
        print('value is zero')
    else:
        result = a / 0.609344
        return result


# 4. Километры в мили
def km_to_mile(a):
    if not type(a) == int and not type(a) == float:
        print("input only digit!")
    elif a == 0:
        print('value is zero')
    else:
        result = a * 0.609344
        return result


# 5. Фунты в килограммы
def pounds_to_kg(a):
    if not type(a) == int and not type(a) == float:
        print("input only digit!")
    elif a == 0:
        print('value is zero')
    else:
        result = a * 0.454
        return result


# 6. Килограммы в фунты
def kg_to_pounds(a):
    if not type(a) == int and not type(a) == float:
        print("input only digit!")
    elif a == 0:
        print('value is zero')
    else:
        result = a / 0.454
        return result


# 7. Унции в граммы
def ounce_to_gr(a):
    if not type(a) == int and not type(a) == float:
        print("input only digit!")
    elif a == 0:
        print('value is zero')
    else:
        result = a * 28.34952312
        return result


# 8. Граммы в унции
def gr_to_ounce(a):
    if not type(a) == int and not type(a) == float:
        print("input only digit!")
    elif a == 0:
        print('value is zero')
    else:
        result = a / 28.34952312
        return result


# 9. Галлон в литры
def gallons_to_liters(a):
    if not type(a) == int and not type(a) == float:
        print("input only digit!")
    elif a == 0:
        print('value is zero')
    else:
        result = a / 4.54609926499
        return result


# 10. Литры в галлоны
def liters_to_gallons(a):
    if not type(a) == int and not type(a) == float:
        print("input only digit!")
    elif a == 0:
        print('value is zero')
    else:
        result = a * 4.54609926499
        return result


# 11. Пинты в литры
def pints_to_liters(a):
    if not type(a) == int and not type(a) == float:
        print("input only digit!")
    elif a == 0:
        print('value is zero')
    else:
        result = a * 0.56826125
        return result


# 12. Литры в пинты
def liters_to_pints(a):
    if not type(a) == int and not type(a) == float:
        print("input only digit!")
    elif a == 0:
        print('value is zero')
    else:
        result = a / 0.56826125
        return result


while True:
    choose = input('\nChoose operation: ')

    if choose == '0':
        break
    elif choose == '':
        print('you must enter number in range 1-12 or 0 to exit!')
        continue
    elif choose == '1':
        print(inch_to_sm(float(input('input number: '))))
    elif choose == '2':
        print(sm_to_inch(float(input('input number: '))))
    elif choose == '3':
        print(mile_to_km(float(input('input number: '))))
    elif choose == '4':
        print(km_to_mile(float(input('input number: '))))
    elif choose == '5':
        print(pounds_to_kg(float(input('input number: '))))
    elif choose == '6':
        print(kg_to_pounds(float(input('input number: '))))
    elif choose == '7':
        print(ounce_to_gr(float(input('input number: '))))
    elif choose == '8':
        print(gr_to_ounce(float(input('input number: '))))
    elif choose == '9':
        print(gallons_to_liters(float(input('input number: '))))
    elif choose == '10':
        print(liters_to_gallons(float(input('input number: '))))
    elif choose == '11':
        print(pints_to_liters(float(input('input number: '))))
    elif choose == '12':
        print(liters_to_pints(float(input('input number: '))))
    else:
        print('input in range 1-12')