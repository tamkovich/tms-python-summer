import task_7_1

while True:

    try:
        flag = input('enter 0 to exit, enter form 1 to 12 to convert:')
        if flag == '0':
            break
        value = float(input('Enter value for converting:'))
    except:
        print('Input error, try again')
        continue

    if flag == '1':
        print(f'{value} inch = {task_7_1.inch_to_cm(value)} cm')
    elif flag == '2':
        print(f'{value} cm = {task_7_1.cm_to_inch(value)} inch')
    elif flag == '3':
        print(f'{value} mile = {task_7_1.mile_to_km(value)} km')
    elif flag == '4':
        print(f'{value} km = {task_7_1.km_to_mile(value)} mile')
    elif flag == '5':
        print(f'{value} funt = {task_7_1.funt_to_kg(value)} kg')
    elif flag == '6':
        print(f'{value} kg = {task_7_1.kg_to_funt(value)} funt')
    elif flag == '7':
        print(f'{value} ounce = {task_7_1.ounce_to_gram(value)} g')
    elif flag == '8':
        print(f'{value} g = {task_7_1.gram_to_ounce(value)} ounce')
    elif flag == '9':
        print(f'{value} gallon = {task_7_1.gallon_to_litre(value)} litre')
    elif flag == '10':
        print(f'{value} litre = {task_7_1.litre_to_gallon(value)} gallon')
    elif flag == '11':
        print(f'{value} pint = {task_7_1.pint_to_litre(value)} litre')
    elif flag == '12':
        print(f'{value} litre = {task_7_1.litre_to_pint(value)} pint')
