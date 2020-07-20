# Написать программу, со следующим интерфейсом: пользователю предоставляется на
# выбор 12 вариантов перевода(описанных в первой задаче). Пользователь вводит цифру
# от одного до двенадцати. После программа запрашивает ввести численное значение.
# Затем программа выдает конвертированный результат. Использовать функции из первого
# задания. Программа должна быть в бесконечном цикле. Код выхода из программы - “0”.

import task_7_1

converter_dict = {
    '1': task_7_1.inch_to_cm,
    '2': task_7_1.cm_to_inch,
    '3': task_7_1.mile_to_km,
    '4': task_7_1.km_to_mile,
    '5': task_7_1.funt_to_kg,
    '6': task_7_1.kg_to_funt,
    '7': task_7_1.ounce_to_gram,
    '8': task_7_1.gram_to_ounce,
    '9': task_7_1.gallon_to_litre,
    '10': task_7_1.litre_to_gallon,
    '11': task_7_1.pint_to_litre,
    '12': task_7_1.litre_to_pint,

}

while True:

    try:
        flag = input('enter 0 to exit, enter form 1 to 12 to convert:')
        if flag == '0':
            break
        value = float(input('Enter value for converting:'))
    except:
        print('Input error, try again')
        continue

    print(f'{value} litre = {converter_dict[flag](value)} pint')
