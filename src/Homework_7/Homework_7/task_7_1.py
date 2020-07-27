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
