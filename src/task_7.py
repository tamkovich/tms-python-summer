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
# 2. Написать программу, со следующим интерфейсом: пользователю предоставляется на
# выбор 12 вариантов перевода(описанных в первой задаче). Пользователь вводит цифру
# от одного до двенадцати. После программа запрашивает ввести численное значение.
# Затем программа выдает конвертированный результат. Использовать функции из первого
# задания. Программа должна быть в бесконечном цикле. Код выхода из программы - “0”

def duim_v_sant(duim):
    sant = duim * 2.54
    print(f"В {duim} дюймах {sant} сантимантов")
    return sant, duim

def sant_v_duim(sant):
    duim = sant / 2.54
    print(f"В {sant} сантимантрах {duim} дюймов ")
    return duim, sant


def mili_v_kilom(mili):
    kilom = mili * 1.609
    print(f"В {mili} милях {kilom} километров")
    return mili, kilom


def kilom_v_mili(kilom):
    mili = kilom / 1.609
    print(f"В {kilom} километрах {mili} миль")
    return kilom, mili


def funt_v_kilog(funt):
    kilog = funt / 2.205
    print(f"В {funt} фунтах {kilog} килограмм")
    return funt, kilog


def kilog_v_funt(kilog):
    funt = kilog * 2.205
    print(f"В {kilog} килограммах {funt} фунтов")
    return kilog, funt


def uncii_v_gramm(uncii):
    gramm = uncii / 0.0353
    print(f"В {uncii} унциях {gramm} грамм")
    return uncii, gramm


def gramm_v_uncii(gramm):
    uncii = gramm * 0.0353
    print(f"В {gramm} граммах {uncii} унций")
    return gramm, uncii


def gallon_v_litr(gallon):
    litr = gallon * 3.785
    print(f"В {gallon} галлонах {litr} литров")
    return gallon, litr


def litr_v_gallon(litr):
    gallon = litr / 3.785
    print(f"В {litr} литрах {gallon} галлонов")
    return litr, gallon


def pint_v_litr(pint):
    litr = pint / 0.568261
    print(f"В {pint} пинтах {litr} литров")
    return pint, litr


def litr_v_pint(litr):
    pint = litr * 0.568261
    print(f"В {litr} литрах {pint} пинт")
    return litr, pint

while True:
    print('1. Дюймы в сантиметры\n'
          '2. Сантиметры в дюймы\n'
          '3. Мили в километры\n'
          '4. Километры в мили\n'
          '5. Фунты в килограммы\n'
          '6. Килограммы в фунты\n'
          '7. Унции в граммы\n'
          '8. Граммы в унции\n'
          '9. Галлон в литры\n'
          '10. Литры в галлоны\n'
          '11. Пинты в литры\n'
          '12. Литры в пинты\n')

    x = int(input('Выберите операцию(Введите номер операции): '))

    if x == 1:
        y = int(input('Введите количество дюймов: '))
        duim_v_sant(y)
        print()
    elif x == 2:
        y = int(input('Введите количество сантиметров: '))
        sant_v_duim(y)
        print()
    elif x == 3:
        y = int(input('Введите количество миль: '))
        mili_v_kilom(y)
        print()
    elif x == 4:
        y = int(input('Введите количество километров: '))
        kilom_v_mili(y)
        print()
    elif x == 5:
        y = int(input('Введите количество фунтов: '))
        funt_v_kilog(y)
        print()
    elif x == 6:
        y = int(input('Введите количество килограмм: '))
        kilog_v_funt(y)
        print()
    elif x == 7:
        y = int(input('Введите количество унций: '))
        uncii_v_gramm(y)
        print()
    elif x == 8:
        y = int(input('Введите количество грамм: '))
        gramm_v_uncii(y)
        print()
    elif x == 9:
        y = int(input('Введите количество галлонов: '))
        gallon_v_litr(y)
        print()
    elif x == 10:
        y = int(input('Введите количество литров: '))
        litr_v_gallon(y)
        print()
    elif x == 11:
        y = int(input('Введите количество пинт: '))
        pint_v_litr(y)
        print()
    elif x == 12:
        y = int(input('Введите количество литров: '))
        litr_v_pint(y)
        print()
    else:
        print('Введите число от 1 до 12')
        continue
    if True:
        stop = int(input('Если хотете остановить операцию, введите 0: '))
        if stop == 0:
            break