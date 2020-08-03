# csv_utils
"""Написать функции по работе с csv файлами в файле csv_utils.py. Чтение.
Запись. Добавление записи(по позиции, по-умолчанию в конец). Удаление
записи(по позиции, по-умолчанию последнюю)."""
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
