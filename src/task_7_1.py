'''1. Написать 12 функций :
1. Дюймы в сантиметры 2. Сантиметры в дюймы 3. Мили в километры
4. Километры в мили   5. Фунты в килограммы 6. Килограммы в фунты
7. Унции в граммы     8. Граммы в унции     9. Галлон в литры
10. Литры в галлоны   11. Пинты в литры     12. Литры в пинты'''

def inch_cm(value: float) -> float:
    # Дюймы в сантиметры
    return value * 2.54

def cm_inch(value: float) -> float:
    # Cантиметры в дюймы
    return value / 2.54

def mile_km(value: float) -> float:
    # Мили в километры
    return value * 1.609

def km_mile(value: float) -> float:
    # Километры в мили
    return value / 1.609

def pounds_kg(value: float) -> float:
    # Фунты в килограммы
    return value * 2.205

def kg_pounds(value: float) -> float:
    # Киллограммы в фунты
    return value / 2.205

def ounce_g(value: float) -> float:
    # Унции в граммы
    return value * 28.35

def g_ounce(value: float) -> float:
    # Граммы в унции
    return value / 28.35

def gallon_l(value: float) -> float:
    # Галлон в литр
    return value * 3.785

def l_gallon(value: float) -> float:
    # Литр в галлон
    return value / 3.785

def pints_l(value: float) -> float:
    # Пинты в литры
    return value * 2.113

def l_pints(value: float) -> float:
    # Литры в пинту
    return value / 2.113
