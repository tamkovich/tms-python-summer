# task_7_1
"""Написать 12 функций по переводу"""


def inch_cm(value: float) -> float:
    """
    The function converts from inch to cm
    :param value: value in inch
    :return: value in cm
    """
    return value * 2.54


def cm_inch(value: float) -> float:
    """
    The function converts from cm to inch
    :param value: value in cm
    :return: value in inch
    """
    return value / 2.54


def mile_km(value: float) -> float:
    """
    The function converts from mile to km
    :param value: value in mile
    :return: value in km
    """
    return value * 1.609


def km_mile(value: float) -> float:
    """
    The function converts from km to mile
    :param value: value in km
    :return: value in mile
    """
    return value / 1.609


def pounds_kg(value: float) -> float:
    """
    The function converts from pounds to kg
    :param value: value in pounds
    :return: value in kg
    """
    return value * 2.205


def kg_pounds(value: float) -> float:
    """
    The function converts from kg to pounds
    :param value: value in kg
    :return: value in pounds
    """
    return value / 2.205


def ounce_g(value: float) -> float:
    """
    The function converts from ounce to gram
    :param value: value in ounce
    :return: value in gram
    """
    return value * 28.35


def g_ounce(value: float) -> float:
    """
    The function converts from gram to ounce
    :param value: value in gram
    :return: value in ounce
    """
    return value / 28.35


def gallon_l(value: float) -> float:
    """
    The function converts from gallon to liter
    :param value: value in gallon
    :return: value in liter
    """
    return value * 3.785


def l_gallon(value: float) -> float:
    """
    The function converts from liter to gallon
    :param value: value in liter
    :return: value in gallon
    """
    return value / 3.785


def pints_l(value: float) -> float:
    """
    The function converts from pints to liter
    :param value: value in pints
    :return: value in liter
    """
    return value * 2.113


def l_pints(value: float) -> float:
    """
    The function converts from liter to pints
    :param value: value in liter
    :return: value in pints
    """
    return value / 2.113
