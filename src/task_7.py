def du_cm(a):
    c = a * 2.54
    print(c)
    return(c)
def cm_du(a):
    c = a / 2.54
    print(c)
    return(c)
def mi_km(a):
    c = a * 1.60934
    print(c)
    return(c)
def km_mi(a):
    c = a / 1.60934
    print(c)
    return(c)
def fu_kg(a):
    c = a * 0.453592
    print(c)
    return(c)
def kg_fu(a):
    c = a / 0.453592
    print(c)
    return(c)
def un_g(a):
    c = a * 28.3495
    print(c)
    return(c)
def g_un(a):
    c = a / 28.3495
    print(c)
    return(c)
def ga_li(a):
    c = a * 0.219969
    print(c)
    return(c)
def li_ga(a):
    c = a / 0.219969
    print(c)
    return(c)
def pi_li(a):
    c = a * 0.568261
    print(c)
    return(c)
def li_pi(a):
    c = a / 0.568261
    print(c)
    return(c)
while True:
    b = int(input('enter a number in range from 1 to 12 '))
    a = int(input())
    if b == 0:
        break
    if b == 1:
        du_cm(a)
    elif b == 2:
        cm_du(a)
    elif b == 3:
        mi_km(a)
    elif b == 4:
        km_mi(a)
    elif b == 5:
        fu_kg(a)
    elif b == 6:
        kg_fu(a)
    elif b == 7:
        un_g(a)
    elif b == 8:
        g_un(a)
    elif b == 9:
        ga_li(a)
    elif b == 10:
        li_ga(a)
    elif b == 11:
        li_pi(a)
    elif b == 12:
        pi_li(a)








