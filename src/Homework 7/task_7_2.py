# task_7_2
"""Написать программу, со следующим интерфейсом: пользователю предоставляется на
выбор 12 вариантов перевода(описанных в первой задаче). Пользователь вводит цифру
от одного до двенадцати. После программа запрашивает ввести численное значение.
Затем программа выдает конвертированный результат. Использовать функции из первого
задания. Программа должна быть в бесконечном цикле. Код выхода из программы - “0”."""


import task_7_1


def menu():
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

        if value < 0:
            print("Value must be positive")
            continue

        if choice == "1":
            print(f"{value} inch = {task_7_1.inch_cm(value)} cm")
        elif choice == "2":
            print(f"{value} cm = {task_7_1.cm_inch(value)} inch")
        elif choice == "3":
            print(f"{value} miles = {task_7_1.mile_km(value)} km")
        elif choice == "4":
            print(f"{value} km = {task_7_1.km_mile(value)} miles")
        elif choice == "5":
            print(f"{value} pounds = {task_7_1.pounds_kg(value)} kg")
        elif choice == "6":
            print(f"{value} kg = {task_7_1.kg_pounds(value)} pounds")
        elif choice == "7":
            print(f"{value} ounce = {task_7_1.ounce_g(value)} gram")
        elif choice == "8":
            print(f"{value} gram = {task_7_1.g_ounce(value)} ounce")
        elif choice == "9":
            print(f"{value} gallon = {task_7_1.gallon_l(value)} liter")
        elif choice == "10":
            print(f"{value} liter = {task_7_1.l_gallon(value)} gallon")
        elif choice == "11":
            print(f"{value} pints = {task_7_1.pints_l(value)} liter")
        elif choice == "12":
            print(f"{value} liter = {task_7_1.l_pints(value)} pints")
        else:
            print("U should enter 0 or 1-12.")
    except TypeError:
        print("Value or choice not a number.")
        continue
