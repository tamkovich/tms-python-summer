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

def cm_to_inch(x: int) -> str:
    '''
    функция конвертирует сантиметры в дюймы (с округлением до пяти знаков после запятой)
    :param x: int
    :return y: float
    '''
    y = x * .394
    return f'{round(y, 3)} inch'

def inch_to_cm(x: int) -> str:
    '''
    функция конвертирует дюймы в сантиметры (с округлением до пяти знаков после запятой)
    :param x: int
    :return y: float
    '''
    y = x * 2.54
    return f'{round(y, 3)} cm'

def km_to_miles(x: int) -> str:
    '''
    функция конвертирует килоиетры в мили (с округлением до пяти знаков после запятой)
    :param x: int
    :return y: float
    '''
    y = x * .621
    return f'{round(y, 3)} miles'

def miles_to_km(x: int) -> str:
    '''
    функция конвертирует километры в мили (с округлением до пяти знаков после запятой)
    :param x: int
    :return y: float
    '''
    y = x * 1.609
    return f'{round(y, 3)} km'

def pound_to_kg(x: int) -> str:
    '''
    функция конвертирует фунты в килограммы (с округлением до пяти знаков после запятой)
    :param x: int
    :return y: float
    '''
    y = x * .454
    return f'{round(y, 3)} kg'


def kg_to_pound(x: int) -> str:
    '''
    функция конвертирует килограммы в фунты (с округлением до пяти знаков после запятой)
    :param x: int
    :return y: float
    '''
    y = x * 2.205
    return f'{round(y, 3)} pound'


def oz_to_gr(x: int) -> str:
    '''
    функция конвертирует унции в граммы (с округлением до пяти знаков после запятой)
    :param x: int
    :return y: float
    '''
    y = x * 28.35
    return f'{round(y, 3)} gr'


def gr_to_oz(x: int) -> str:
    '''
    функция конвертирует граммы в унции (с округлением до пяти знаков после запятой)
    :param x: int
    :return y: float
    '''
    y = x * 0.0353
    return f'{round(y, 3)} oz'


def hallon_to_litr(x: int) -> str:
    '''
    функция конвертирует галлоны в литры (с округлением до пяти знаков после запятой)
    :param x: int
    :return y: float
    '''
    y = x * 4.546
    return f'{round(y, 3)} l'


def litr_to_hallon(x: int) -> str:
    '''
    функция конвертирует литры в галлоны (с округлением до пяти знаков после запятой)
    :param x: int
    :return y: float
    '''
    y = x * 0.264
    return f'{round(y, 3)} hal'


def pint_to_litr(x: int) -> str:
    '''
    функция конвертирует амер пинты в литры (с округлением до пяти знаков после запятой)
    :param x: int
    :return y: float
    '''
    y = x * .473
    return f'{round(y, 3)} l'


def litr_to_pint(x: int) -> str:
    '''
    функция конвертирует литры в амер пинты (с округлением до пяти знаков после запятой)
    :param x: int
    :return y: float
    '''
    y = x * 2.113
    return f'{round(y, 3)} pnt'

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
        select = int(input('Please enter number convertation from 0 to 12: '))
    except ValueError:
        print("Incorrect input. Try again.")
    finally:
        print(45 * '#')
    if select == 0:
        break
    elif select > 0 and select < 13:
        try:
            x = float(input("Enter value of the seleted quantity: "))
        except ValueError:
            print('You input is no digit!!!! Try again')
        finally:
            print(45 * '#')
        konverter_dict = {
            1: cm_to_inch,
            2: inch_to_cm,
            3: km_to_miles,
            4: miles_to_km,
            5: pound_to_kg,
            6: kg_to_pound,
            7: oz_to_gr,
            8: gr_to_oz,
            9: hallon_to_litr,
            10: litr_to_hallon,
            11: pint_to_litr,
            12: litr_to_pint,
        }
        result = konverter_dict[select](x)
        print(f'value of the convertible quantity: {result}')
    else:
        print("Incorrect input!")
        print("Please select number 0-12")
        continue




