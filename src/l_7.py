def duimvsant(duim):
    sant = duim * 2.54
    print("в" + duim + "дюймах " + sant + "сантиметров")
    return sant, duim


def santvduim(sant):
    duim = sant / 2.54
    print("в" + sant + "сантиметрах" + duim + "дюймов")
    return duim, sant


def milivkm(mili):
    km = mili * 1.609
    print("в" + mili + "милях" + km + "километров")
    return mili, km


def kmvmili(km):
    mili = km / 1.609
    print("в" + km + "километрах " + mili + "миль")
    return km, mili


def funtvkg(funt):
    kg = funt / 2.205
    print("в " + funt + "фунтах" + kg + "килограмм")
    return funt, kg


def kgvfunt(kg):
    funt = kg * 2.205
    print("В " + kg + "килограммах " + funt + "фунтов")
    return kg, funt


def unciivgramm(uncii):
    gramm = uncii / 0.0353
    print("в " + uncii + "унциях " + gramm + "грамм")
    return uncii, gramm


def grammvyncii(gramm):
    uncii = gramm * 0.0353
    print("в " + gramm + "граммах " + uncii + "унций")
    return gramm, uncii


def gallonvlitr(gallon):
    litr = gallon * 3.785
    print("в " + gallon + "галлонах " + litr + "литров")
    return gallon, litr


def litrvgallon(litr):
    gallon = litr / 3.785
    print("в " + litr + "литрах " + gallon + "галлонов")
    return litr, gallon


def pintvlitr(pint):
    litr = pint / 0.568
    print("в " + pint + "пинтах " + litr + "литров")
    return pint, litr


def litrvpint(litr):
    pint = litr * 0.568
    print("в " + litr + "литрах " + pint + "пинт")
    return litr, pint


while True:
    print('1. Дюйм в сантиметры\n'
          '2. Сантиметр в дюйм\n'
          '3. Мили в километры\n'
          '4. Километры в мили\n'
          '5. Фунты в килограммы\n'
          '6. Килограммы в фунты\n'
          '7. Унции в граммы\n'
          '8. Граммы в унции\n'
          '9. Галлоны в литры\n'
          '10. Литры в галлоны\n'
          '11. Пинты в литры\n'
          '12. Литры в пинты\n')

    x = int(input("выбрать операцию: "))
    if x == 1:
        y = int(input("дюймов: "))
        duimvsant(y)
        print()
    elif x == 2:
