# csv_utils
"""Написать функции по работе с csv файлами в файле csv_utils.py. Чтение.
Запись. Добавление записи(по позиции, по-умолчанию в конец). Удаление
записи(по позиции, по-умолчанию последнюю).

Использовать результаты 10.8. Все функции описываются в csv_utils.py.
Проверка работы функции осуществляется в task_10_09.py.
Создать функцию подсчета полной суммы всех товаров.
Создать функцию поиска самого дорогого товара.
Создать функцию самого дешевого товара.
Создать функцию уменьшения количества товара(на n, по-умолчанию на 1)"""
import csv


def csv_read(path: str, arg: str) -> list:
    """
    Open CSV file
    :param path: path of file
    :param arg: type of file
    :return: list of text
    """
    rows = []
    with open(path, arg) as csvfile:
        for row in csv.reader(csvfile):
            rows.append(row)
    return rows


def csv_write(path: str, arg: str, data: list):
    """
    Writes data to CSV file
    :param path: path of file
    :param arg: type of file
    :param data: data for file
    :return: nothing
    """
    with open(path, arg) as csvfile:
        for line in data:
            csv.writer(csvfile).writerow(line)


def csv_append(path: str, data: list, line: int):
    """
    Appends data to CSV file
    :param path: path of file
    :param data: data for append
    :param line: after this line insert data (if -1 at the end)
    :return: nothing
    """
    rows = []
    with open(path, "r") as csvfile:
        for row in csv.reader(csvfile):
            rows.append(row)
    if line == -1:
        rows.append(data)
    else:
        rows.insert(line, data)

    with open(path, "w") as csvfile:
        for i in rows:
            csv.writer(csvfile).writerow(i)


def csv_delete(path: str, line: int):
    """
    Delete some line in CSV file
    :param path: path of file
    :param line: delete this line
    :return: nothing
    """
    rows = []
    with open(path, "r") as csvfile:
        for row in csv.reader(csvfile):
            rows.append(row)

    del rows[line]

    with open(path, "w") as csvfile:
        for row in rows:
            csv.writer(csvfile).writerow(row)


def sum_of_price(path: str) -> int:
    """
    Total sum of all prices of products
    :param path: path of file
    :return: sum of prices
    """
    summa = 0
    list_of_product = csv_read(path, "r")
    for line in range(1, len(list_of_product)):
        try:
            summa += int(list_of_product[line][1])
        except ValueError:
            print("Price not a number")
            return 0
    return summa


def search(path: str, arg: str) -> str:
    """
    Function search the most expensive product
    :param arg: max or min
    :param path: path of file
    :return: name of product, price of product
    """
    list_of_product = csv_read(path, "r")
    list_of_prices = []

    for line in range(1, len(list_of_product)):
        list_of_prices.append(list_of_product[line][1])

    if arg == "max":
        value = max(list_of_prices)
    elif arg == "min":
        value = min(list_of_prices)
    else:
        print("Arg must be max or min")
        return "error"

    index = list_of_prices.index(value)

    return list_of_product[index + 1][0]


def purchase_of_product(path: str, number: int, name: str) -> bool:
    """
    Reducing the product by number
    :param name: name of product
    :param path: path of file
    :param number: numbers of reducing
    :return: True or False
    """
    list_of_product = csv_read(path, "r")
    check = True
    for line in range(1, len(list_of_product)):
        try:
            list_of_product[line][2] = int(list_of_product[line][2])
        except ValueError:
            return False

        if name == list_of_product[line][0]:
            list_of_product[line][2] -= number
            csv_write(path, "w", list_of_product)
            return True
        else:
            check = False

    if not check:
        return False
