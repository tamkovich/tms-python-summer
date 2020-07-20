while True:
    user_input = input("input operator(+,-,*,/):")  # ввести знак желаемой операции над введенными числами

    """ввести два числа: x, y"""
    x = int(input("operand_x:"))
    y = int(input("operand_y:"))

    if user_input == '0':  # выход из цикла
        break
        print("quit operation")

    elif user_input == '+':
        z = x + y
        print(f'{x} + {y} = {z}')
    elif user_input == '-':
        z = x - y
        print(f'{x} - {y} = {z}')
    elif user_input == '*':
        z = x * y
        print(f'{x} * {y} = {z}')
    elif user_input == '/':
        if y == 0:
            print("Error, division by zero.")
            continue
        else:
            z = x / y
            print(f'{x} / {y} = {z}')

    else:
        print("incorrect operator, try again")
        continue
