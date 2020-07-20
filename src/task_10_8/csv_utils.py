"""Написать функции по работе с csv файлами в файле csv_utils.py. Чтение.
Запись. Добавление записи(по позиции, по-умолчанию в конец). Удаление
записи(по позиции, по-умолчанию последнюю).
В файле task_10_08 импортировать функции. С помощью функций создать
файл с информацией о товарах(Имя товара, цена, количество,
комментарий).
Прочесть файл, Добавить новую позицию в конец. Удалить третью строку."""

import csv


def read_csv(file_path: str) -> list:
    """
    reads data a file and returns it
    :param file_path: path to a file
    :return rows: list of strings of a file data
    """
    rows = []
    with open(file_path, 'r') as my_file:
        csv_reader = csv.reader(my_file)
        for row in csv_reader:
            rows.append(row)
    return rows


def write_csv(file_path: str, data: list) -> list:
    """
    writes data in a file
    :param file_path: path to file in which data will be written
    :param data: data which which data will be written
    """
    with open(file_path, 'w', newline='') as my_file:
        csv_writer = csv.writer(my_file)
        csv_writer.writerows(data)


def add_csv(file_path: str, row: list, position=-1):
    """
    adds row to a file on line with number 'position' or end if position = -1
    :param file_path: path to file in which row will be written
    :param position: number of line in which row will be written
    """
    if position == -1:
        with open(file_path, 'a', newline='') as my_file:
            csv_writer = csv.writer(my_file)
            csv_writer.writerow(row)
    else:
        rows = read_csv(file_path)
        rows.insert(position, row)
        write_csv(file_path, rows)


def delete_csv(file_path: str, position=-1):
    """
    delete row from a file on line with number 'position' or end if position = -1
    :param file_path: path to file in which row will be deleted
    :param position: number of line in which row will be deleted
    """
    if position == -1:
        rows = read_csv(file_path)
        del rows[-1]
        write_csv(file_path, rows)
    else:
        rows = read_csv(file_path)
        del rows[position]
        write_csv(file_path, rows)


if __name__ == '__main__':
    print(read_csv('data.csv'))
    write_csv('saved_data.csv', read_csv('data.csv'))
    add_csv('saved_data_2.csv', [2000, 'Jeep_1', 'My New Car', "MUST SELL! air_, moon roof 2, loaded", 6799.00], 0)
    delete_csv('saved_data_3.csv', 0)
