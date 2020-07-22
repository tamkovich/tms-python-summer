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
	if x < 0:
		return None
    try:
        return x * 2.54
    except:
        return None


def cm_to_inch(x: float) -> float:
	if x < 0:
		return None
    try:
        return x / 2.54
    except:
        return None


def mile_to_km(x: float) -> float:
	if x < 0:
		return None
    try:
        return x * 1.60934
    except:
        return None


def km_to_mile(x: float) -> float:
	if x < 0:
		return None
    try:
        return x / 1.60934
    except:
        return None


def funt_to_kg(x: float) -> float:
	if x < 0:
		return None
    try:
        return x * 0.409517
    except:
        return None


def kg_to_funt(x: float) -> float:
	if x < 0:
		return None
    try:
        return x / 0.409517
    except:
        return None


def ounce_to_gram(x: float) -> float:
	if x < 0:
		return None
    try:
        return x * 28.3495
    except:
        return None


def gram_to_ounce(x: float) -> float:
	if x < 0:
		return None
    try:
        return x / 28.3495
    except:
        return None


def gallon_to_litre(x: float) -> float:
	if x < 0:
		return None
    try:
        return x * 3.78541
    except:
        return None


def litre_to_gallon(x: float) -> float:
	if x < 0:
		return None
    try:
        return x / 3.78541
    except:
        return None


def pint_to_litre(x: float) -> float:
	if x < 0:
		return None
    try:
        return x * 0.473176
    except:
        return None


def litre_to_pint(x: float) -> float:
	if x < 0:
		return None
    try:
        return x / 0.473176
    except:
        return None

