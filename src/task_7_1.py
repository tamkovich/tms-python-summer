def inch_to_sm(a: int) -> float:
    """
    1. Дюймы в сантиметры
    :param a: Дюймы
    :return: сантиметры
    """
    return a / 0.39


def sm_to_inch(a: int) -> float:
    """
    2. Сантиметры в дюймы
    :param a: Сантиметры
    :return: дюймы
    """
    return a * 0.39


def mile_to_km(a: int) -> float:
    """
    3. Мили в километры
    :param a: Мили
    :return: километры
    """
    return a / 0.609344


def km_to_mile(a: int) -> float:
    """
    4. Километры в мили
    :param a: Километры
    :return: мили
    """
    return a * 0.609344


def pounds_to_kg(a: int) -> float:
    """
    5. Фунты в килограммы
    :param a: Фунты
    :return: килограммы
    """
    return a * 0.454


def kg_to_pounds(a: int) -> float:
    """
    6. Килограммы в фунты
    :param a: Килограммы
    :return: фунты
    """
    return a / 0.454


def ounce_to_gr(a: int) -> float:
    """
    7. Унции в граммы
    :param a: Унции
    :return: граммы
    """
    return a * 28.34952312


def gr_to_ounce(a: int) -> float:
    """
    8. Граммы в унции
    :param a: Граммы
    :return: унции
    """
    return a / 28.34952312


def gallons_to_liters(a: int) -> float:
    """
    9. Галлон в литры
    :param a: Галлон
    :return: литры
    """
    return a / 4.54609926499


def liters_to_gallons(a: int) -> float:
    """
    10. Литры в галлоны
    :param a: Литры
    :return: галлоны
    """
    return a * 4.54609926499


def pints_to_liters(a: int) -> float:
    """
    11. Пинты в литры
    :param a:Пинты
    :return:литры
    """
    return a * 0.56826125


def liters_to_pints(a: int) -> float:
    """
    12. Литры в пинты
    :param a: Литры
    :return: пинты
    """
    return a / 0.56826125


while True:
    try:
        choose = input('\nChoose operation: ')
        if choose == "0":
            break
        elif 0 < int(choose) < 13:
            number = float(input('input number: '))
        else:
            print('input in range 1-12')
            continue
    except ValueError:
        print('error input!')
        continue
    switch_case = {
        "1": inch_to_sm,
        "2": sm_to_inch,
        "3": mile_to_km,
        "4": km_to_mile,
        "5": pounds_to_kg,
        "6": kg_to_pounds,
        "7": ounce_to_gr,
        "8": gr_to_ounce,
        "9": gallons_to_liters,
        "10": liters_to_gallons,
        "11": pints_to_liters,
        "12": liters_to_pints,
    }
    result = switch_case.get(choose)(number)
    print(round(result, 3))
