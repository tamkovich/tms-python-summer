def inch_to_cm(x: float) -> float:
    try:
        return x * 2.54
    except:
        return None


def cm_to_inch(x: float) -> float:
    try:
        return x / 2.54
    except:
        return None


def mile_to_km(x: float) -> float:
    try:
        return x * 1.60934
    except:
        return None


def km_to_mile(x: float) -> float:
    try:
        return x / 1.60934
    except:
        return None


def funt_to_kg(x: float) -> float:
    try:
        return x * 0.409517
    except:
        return None


def kg_to_funt(x: float) -> float:
    try:
        return x / 0.409517
    except:
        return None


def ounce_to_gram(x: float) -> float:
    try:
        return x * 28.3495
    except:
        return None


def gram_to_ounce(x: float) -> float:
    try:
        return x / 28.3495
    except:
        return None


def gallon_to_litre(x: float) -> float:
    try:
        return x * 3.78541
    except:
        return None


def litre_to_gallon(x: float) -> float:
    try:
        return x / 3.78541
    except:
        return None


def pint_to_litre(x: float) -> float:
    try:
        return x * 0.473176
    except:
        return None


def litre_to_pint(x: float) -> float:
    try:
        return x / 0.473176
    except:
        return None
