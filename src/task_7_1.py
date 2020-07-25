# 1. Дюймы в сантиметры
def inch_to_sm(a):
    return a / 0.39


# 2. Сантиметры в дюймы
def sm_to_inch(a):
    return a * 0.39


# 3. Мили в километры
def mile_to_km(a):
    return a / 0.609344


# 4. Километры в мили
def km_to_mile(a):
    return a * 0.609344


# 5. Фунты в килограммы
def pounds_to_kg(a):
    return a * 0.454


# 6. Килограммы в фунты
def kg_to_pounds(a):
    return a / 0.454


# 7. Унции в граммы
def ounce_to_gr(a):
    return a * 28.34952312


# 8. Граммы в унции
def gr_to_ounce(a):
    return a / 28.34952312


# 9. Галлон в литры
def gallons_to_liters(a):
    return a / 4.54609926499


# 10. Литры в галлоны
def liters_to_gallons(a):
    return a * 4.54609926499


# 11. Пинты в литры
def pints_to_liters(a):
    return a * 0.56826125


# 12. Литры в пинты
def liters_to_pints(a):
    return a / 0.56826125


while True:
    choose = input('\nChoose operation: ')
    try:
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
    except ValueError:
        print('error input!')