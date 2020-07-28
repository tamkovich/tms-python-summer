"""
Написать программу, в которой вводятся два операнда Х и Y и знак операции
sign (+, –, /, *). Вычислить результат Z в зависимости от знака. Предусмотреть
реакции на возможный неверный знак операции, а также на ввод Y=0 при
делении. Организовать возможность многократных вычислений без перезагрузки
программа (т.е. построить бесконечный цикл). В качестве символа прекращения
вычислений принять ‘0’ (т.е. sign='0').
"""
while True:
    user_input = input("input operator(+,-,*,/):")  # ввести знак желаемой операции над введенными числами
    """ввести два числа: x, y"""
    x = int(input("operand_x:"))
    y = int(input("operand_y:"))

    if user_input == '0':  # выход из цикла
        break

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
