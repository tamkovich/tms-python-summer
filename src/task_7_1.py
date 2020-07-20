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

def inch_to_cm(x: float) -> float:
    """
    converts inch to cm; if x < 0 return None
    :param x: length in inch
    :return: length in cm
    """
    if x < 0:
        return None

    try:
        return x * 2.54
    except:
        return None


def cm_to_inch(x: float) -> float:
    """
    converts cm to inch; if x < 0 return None
    :param x: length in cm
    :return: length in inch
    """
    if x < 0:
        return None

    try:
        return x / 2.54
    except:
        return None


def mile_to_km(x: float) -> float:
    """
    converts mile to km; if x < 0 return None
    :param x: length in mile
    :return: length in km
    """
    if x < 0:
        return None

    try:
        return x * 1.60934
    except:
        return None


def km_to_mile(x: float) -> float:
    """
    converts km to mile; if x < 0 return None
    :param x: length in km
    :return: length in mile
    """
    if x < 0:
        return None

    try:
        return x / 1.60934
    except:
        return None


def funt_to_kg(x: float) -> float:
    """
    converts funt to kg; if x < 0 return None
    :param x: weight in funt
    :return: weight in kg
    """
    if x < 0:
        return None

    try:
        return x * 0.409517
    except:
        return None


def kg_to_funt(x: float) -> float:
    """
    converts kg to funt; if x < 0 return None
    :param x: weight in kg
    :return: weight in funt
    """
    if x < 0:
        return None

    try:
        return x / 0.409517
    except:
        return None


def ounce_to_gram(x: float) -> float:
    """
    converts ounce to gram; if x < 0 return None
    :param x: weight in ounce
    :return: weight in gram
    """
    if x < 0:
        return None

    try:
        return x * 28.3495
    except:
        return None


def gram_to_ounce(x: float) -> float:
    """
    converts gram to ounce; if x < 0 return None
    :param x: weight in gram
    :return: weight in ounce
    """
    if x < 0:
        return None

    try:
        return x / 28.3495
    except:
        return None


def gallon_to_litre(x: float) -> float:
    """
    converts gallon to litre; if x < 0 return None
    :param x: volume in gallon
    :return: volume in litre
    """
    if x < 0:
        return None

    try:
        return x * 3.78541
    except:
        return None


def litre_to_gallon(x: float) -> float:
    """
    converts litre to gallon; if x < 0 return None
    :param x: volume in litre
    :return: volume in gallon
    """
    if x < 0:
        return None

    try:
        return x / 3.78541
    except:
        return None


def pint_to_litre(x: float) -> float:
    """
    converts pint to litre; if x < 0 return None
    :param x: volume in pint
    :return: volume in litre
    """
    if x < 0:
        return None

    try:
        return x * 0.473176
    except:
        return None


def litre_to_pint(x: float) -> float:
    """
    converts litre to pint; if x < 0 return None
    :param x: volume in litre
    :return: volume in pint
    """
    if x < 0:
        return None

    try:
        return x / 0.473176
    except:
        return None
