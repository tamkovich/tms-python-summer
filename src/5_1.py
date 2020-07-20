# task 1_1
"""Написать программу, в которой вводятся два операнда Х и Y и знак операции
sign (+, –, /, *). Вычислить результат Z в зависимости от знака. Предусмотреть
реакции на возможный неверный знак операции, а также на ввод Y=0 при
делении. Организовать возможность многократных вычислений без перезагрузки
программа (т.е. построить бесконечный цикл). В качестве символа прекращения
вычислений принять ‘0’ (т.е. sign='0')."""


def check_digit(tmp: str) -> bool:
    return tmp.isdigit()


while True:
    sign = input("Enter sign (+, -, *, /, 0 - for exit) = ")
    x = input("Enter x = ")
    y = input("Enter y = ")

    if check_digit(x) and check_digit(y):
        x, y = int(x), int(y)

        if sign == "+":
            print(f"{x} + {y} = {x + y}")

        elif sign == "-":
            print(f"{x} - {y} = {x - y}")

        elif sign == "*":
            print(f"{x} * {y} = {x * y}")

        elif sign == "/":
            try:
                print(f"{x} / {y} = {x / y}")
            except ZeroDivisionError:
                print("U can't divide by zero")

        elif sign == "0":
            exit()

        else:
            print("U entered other operator")
            continue
else:
    print("x and y should be numbers")
