# task_7_2
"""Написать программу, со следующим интерфейсом:
пользователю предоставляется на выбор 12 вариантов
перевода(описанных в первой задаче). Пользователь
вводит цифру от одного до двенадцати. После программа
запрашивает ввести численное значение. Затем программа
выдает конвертированный результат. Использовать
функции из первого задания. Программа должна быть
в бесконечном цикле. Код выхода из программы - “0”."""

import task_7_1


def menu():
    """
    The function output menu of program
    :return: nothing
    """
    print("Choose what you need:")
    print("1. Inch to cm.\n2. Cm to inch.")
    print("3. Miles to km.\n4. Km to miles.")
    print("5. Pounds to kg.\n6. Kg to pounds.")
    print("7. Ounce to gram.\n8. Gram to ounce.")
    print("9. Gallon to liter.\n10. Liter to gallon.")
    print("11. Pints to liter.\n12. Liter to pints.")
    print("0. Exit")


while True:
    menu()
    choice = input("Ur choice: ")

    if choice == "0":
        exit()

    value = input("Enter value: ")

    try:
        value = float(value)
    except TypeError:
        print("Value not a number.")
        continue

    converter_dict = {
        "1": task_7_1.inch_cm,
        "2": task_7_1.cm_inch,
        "3": task_7_1.mile_km,
        "4": task_7_1.km_mile,
        "5": task_7_1.pounds_kg,
        "6": task_7_1.kg_pounds,
        "7": task_7_1.ounce_g,
        "8": task_7_1.g_ounce,
        "9": task_7_1.gallon_l,
        "10": task_7_1.l_gallon,
        "11": task_7_1.pints_l,
        "12": task_7_1.l_pints
    }

    if 0 < int(choice) < 13:
        print(converter_dict[choice](value))
    else:
        print("Choice must be >0 and <13")
