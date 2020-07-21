x = int(input('Введите число 1\n'))
z = input('Введите знак операции(+, –, /, *)\n')
y = int(input('Введите число 2\n'))
while True:

    if z == '+':
        summa = x+y
        print(f'{x} {z} {y} = {summa} ')
        sign = int(input('Введите число 0, если хотите прекратить вычисления '))
        if sign == 0:
            break
        x = int(input('Введите число 1\n'))
        z = input('Введите знак операции(+, –, /, *)\n')
        y = int(input('Введите число 2\n'))

    elif z == '-':
        raznost = x-y
        print(f'{x} {z} {y} = {raznost} ')
        sign = int(input('Введите число 0, если хотите прекратить вычисления '))
        if sign == 0:
            break
        x = int(input('Введите число 1\n'))
        z = input('Введите знак операции(+, –, /, *)\n')
        y = int(input('Введите число 2\n'))

    elif z == '/':
        chastnoe = x/y
        print(f'{x} {z} {y} = {chastnoe} ')
        sign = int(input('Введите число 0, если хотите прекратить вычисления '))
        if sign == 0:
            break
        x = int(input('Введите число 1\n'))
        z = input('Введите знак операции(+, –, /, *)\n')
        y = int(input('Введите число 2\n'))
        if y == 0:
            print('Деление на 0 запрещено')
            continue

    elif z == '*':
        proizvedenie = x*y
        print(f'{x} {z} {y} = {proizvedenie} ')
        sign = int(input('Введите число 0, если хотите прекратить вычисления '))
        if sign == 0:
            break
        x = int(input('Введите число 1\n'))
        z = input('Введите знак операции(+, –, /, *)\n')
        y = int(input('Введите число 2\n'))
        if y == 0:
            print('Деление на 0 запрещено')
            continue

    else:
        print('Некорректный знак операции')
        sign = int(input('Введите число 0, если хотите прекратить вычисления '))
        if sign == 0:
            break
        x = int(input('Введите число 1\n'))
        z = input('Введите знак операции(+, –, /, *)\n')
        y = int(input('Введите число 2\n'))
