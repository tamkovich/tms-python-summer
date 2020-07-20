# Написать программу, в которой вводятся два операнда Х и Y и знак операции
# sign (+, –, /, *). Вычислить результат Z в зависимости от знака. Предусмотреть
# реакции на возможный неверный знак операции, а также на ввод Y=0 при
# делении. Организовать возможность многократных вычислений без перезагрузки
# программа (т.е. построить бесконечный цикл). В качестве символа прекращения
# вычислений принять ‘0’ (т.е. sign='0').


def separate_string(input_str: str) -> list:
    """
    split a string into two integer number

    :param input_str: string containing two integer number separated with space
    :return: list with int x and y or -1 when error
    """
    try:
        x, y = input_str.split()
        return int(x), int(y)
    except:
        return -1


while True:
    # inputting and checking data
    xy = input("Enter 'x' and 'y' separated with space or 'exit' to exit, please:")

    if xy == "exit":
        break

    try:
        x, y = separate_string(xy)
    except:
        print("Error input data, try again")
        continue

    # result calculating
    while True:
        control_flag = input(
            "Enter one of the next command '+', '-', '*', '/' or enter 'exit' to exit, please:"
        )

        if control_flag == "+":
            print(f"x + y = {x + y}")
            break
        elif control_flag == "-":
            print(f"x - y = {x - y}")
            break
        elif control_flag == "*":
            print(f"x * y = {x * y}")
            break
        elif control_flag == "/":
            if y != 0:
                print(f"x / y = {x / y}")
                break
            else:
                print("dividing by zero")
                break
        elif control_flag == "exit":
            break
        else:
            print("Input error, try again")
            continue

    # waiting next command
    wait_flag = input("enter 'exit' to exit or any command to continue:")
    if wait_flag == "exit":
        break
