'''
A. Написать 12 функций по переводу:
    1. Дюймы в сантиметры
    2. Сантиметры в дюймы
    3. Мили в километры
    4. Километры в мили
    5. Фунты в килограммы
    6. Килограммы в фунты
    7. Унции в граммы
    8. Граммы в унции
    9. Галлон в литры
    10. Литры в галлоны
    11. Пинты в литры
    12. Литры в пинты
'''

def cm_to_inch(x: int) -> float:
    '''
    функция конвертирует сантиметры в дюймы (с округлением до пяти знаков после запятой)
    :param x: int
    :return y: float
    '''
    y = x * .394
    return round(y, 3)

def inch_to_cm(x: int) -> float:
    '''
    функция конвертирует дюймы в сантиметры (с округлением до пяти знаков после запятой)
    :param x: int
    :return y: float
    '''
    y = x * 2.54
    return round(y, 3)

def km_to_miles(x: int) -> float:
    '''
    функция конвертирует килоиетры в мили (с округлением до пяти знаков после запятой)
    :param x: int
    :return y: float
    '''
    y = x * .621
    return round(y, 3)

def miles_to_km(x: int) -> float:
    '''
    функция конвертирует километры в мили (с округлением до пяти знаков после запятой)
    :param x: int
    :return y: float
    '''
    y = x * 1.609
    return round(y, 3)

def pound_to_kg(x: int) -> float:
    '''
    функция конвертирует фунты в килограммы (с округлением до пяти знаков после запятой)
    :param x: int
    :return y: float
    '''
    y = x * .454
    return round(y, 3)


def kg_to_pound(x: int) -> float:
    '''
    функция конвертирует килограммы в фунты (с округлением до пяти знаков после запятой)
    :param x: int
    :return y: float
    '''
    y = x * 2.205
    return round(y, 3)


def oz_to_gr(x: int) -> float:
    '''
    функция конвертирует унции в граммы (с округлением до пяти знаков после запятой)
    :param x: int
    :return y: float
    '''
    y = x * 28.35
    return round(y, 3)


def gr_to_oz(x: int) -> float:
    '''
    функция конвертирует граммы в унции (с округлением до пяти знаков после запятой)
    :param x: int
    :return y: float
    '''
    y = x * 0.0353
    return round(y, 3)


def hallon_to_litr(x: int) -> float:
    '''
    функция конвертирует галлоны в литры (с округлением до пяти знаков после запятой)
    :param x: int
    :return y: float
    '''
    y = x * 4.546
    return round(y, 3)


def litr_to_hallon(x: int) -> float:
    '''
    функция конвертирует литры в галлоны (с округлением до пяти знаков после запятой)
    :param x: int
    :return y: float
    '''
    y = x * 0.264
    return round(y, 3)


def pint_to_litr(x: int) -> float:
    '''
    функция конвертирует амер пинты в литры (с округлением до пяти знаков после запятой)
    :param x: int
    :return y: float
    '''
    y = x * .473
    return round(y, 3)


def litr_to_pint(x: int) -> float:
    '''
    функция конвертирует литры в амер пинты (с округлением до пяти знаков после запятой)
    :param x: int
    :return y: float
    '''
    y = x * 2.113
    return round(y, 3)

'''
B. Написать программу, со следующим интерфейсом: пользователю предоставляется на
выбор 12 вариантов перевода(описанных в первой задаче). Пользователь вводит цифру
от одного до двенадцати. После программа запрашивает ввести численное значение.
Затем программа выдает конвертированный результат. Использовать функции из первого
задания. Программа должна быть в бесконечном цикле. Код выхода из программы - “0”.
'''

while True:
    print(
"""
Сделайте выбор для конвертации
1<->2: см <-> дюймы; 3<->4: км <-> мили; 5<->6: футы <-> кг, 7<->8: унции <-> граммы;
9<->10: галлоны <-> литры; 11<->12: амер.пинты <-> литры; 0 - выход.
"""
    )
    try:
        select = int(input('Please enter number konvertation from 0 to 12: '))
    except ValueError:
        print("Incorrect input. Try again.")
    finally:
        print(20 * '#')
    if select == 0:
        break
    elif select > 0 and select < 13:
        try:
            x = float(input("Enter value: "))
        except ValueError:
            print('You input is no digit!!!! Try again')
        finally:
            print(20 * '#')
        konverter_dict = {
            1: f'{cm_to_inch(x)} inch',
            2: f'{inch_to_cm(x)} cm',
            3: f'{km_to_miles(x)} mls',
            4: f'{miles_to_km(x)} km',
            5: f'{pound_to_kg(x)} kg',
            6: f'{kg_to_pound(x)} pound',
            7: f'{oz_to_gr(x)} gr',
            8: f'{gr_to_oz(x)} oz',
            9: f'{hallon_to_litr(x)} l',
            10: f'{litr_to_hallon(x)} hal',
            11: f'{pint_to_litr(x)} l',
            12: f'{litr_to_pint(x)} pnt',
        }
        for key, value in konverter_dict.items():
            if select == key:
                print(value)


    else:
        print("Incorrect input!")
        print("Please select number 0-12")
        continue



