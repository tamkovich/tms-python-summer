# Написать программу, в которой вводятся два операнда Х и Y и знак операции
# sign (+, –, /, *). Вычислить результат Z в зависимости от знака. Предусмотреть
# реакции на возможный неверный знак операции, а также на ввод Y=0 при
# делении. Организовать возможность многократных вычислений без перезагрузки
# программа (т.е. построить бесконечный цикл). В качестве символа прекращения
# вычислений принять ‘0’ (т.е. sign='0').


def calc(x, y):
    while True:
        sign = input("Input sign (+, –, /, *): ")
        if sign == "+":
            z = x + y
            print(z)
            break
        elif sign == "-":
            z = x - y
            print(z)
            break
        elif sign == "/":
            if y == 0 or x == 0:
                print("Zero Division Error")
                break
            z = x / y
            print(z)
            break
        elif sign == "*":
            z = x * y
            print(z)
            break
        else:
            print("Wrong operation!")
            continue


while True:
    x = input("X: ")
    y = input("Y: ")
    if x == "q" or y == "q":
        break
    try:
        x = float(x)
        y = float(y)
    except ValueError:
        print("You must enter a number")
        continue

    z = 0
    calc(x, y)
