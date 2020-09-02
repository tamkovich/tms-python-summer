"""Использовать результаты 10.8. Все функции описываются в csv_utils.py.
Проверка работы функции осуществляется в task_10_09.py.
1) Создать функцию подсчета полной суммы всех товаров.
2) Создать функцию поиска самого дорогого товара.
3) Создать функцию самого дешевого товара.
4) Создать функцию уменьшения количества товара(на n, по-умолчанию на 1)"""

from src.task_10_8 import csv_utils


def calc_count(file_path: str) -> int:
    """
    calcs number of goods information about which contains in file with path 'file_path'
    :param file_path: path to a file
    """
    count = 0
    data = csv_utils.read_csv(file_path)

    for i in range(1, len(data)):
        count += int(data[i][2])

    return count


def max_prise(file_path: str) -> str:
    """
    finds a good with max price;
    information about goods contains in file with path 'file_path'
    :param file_path: path to a file
    """
    data = csv_utils.read_csv(file_path)
    dict_data = {}
    position = 0

    for i in data[0]:
        dict_data[i] = [data[k][position] for k in range(1, len(data))]
        position += 1

    return dict_data['name'][(dict_data['price'].index(max(dict_data['price'])))]


def min_prise(file_path: str) -> str:
    """
    finds a good with min price;
    information about goods contains in file with path 'file_path'
    :param file_path: path to a file
    """
    data = csv_utils.read_csv(file_path)
    dict_data = {}
    position = 0

    for i in data[0]:
        dict_data[i] = [data[k][position] for k in range(1, len(data))]
        position += 1

    return dict_data['name'][(dict_data['price'].index(min(dict_data['price'])))]


def change_good_count(file_path: str, new_file_path: str, good_name: str, n=-1):
    """
    changes a good count
    """
    data = csv_utils.read_csv(file_path)
    dict_data = {}
    position = 0

    for i in data[0]:
        dict_data[i] = [data[k][position] for k in range(1, len(data))]
        position += 1

    index_ = dict_data['name'].index(good_name)
    data[index_ + 1][2] = int(data[index_ + 1][2]) + n
    csv_utils.write_csv(new_file_path, data)


print(calc_count('goods.csv'))
print(max_prise('goods.csv'))
print(min_prise('goods.csv'))
change_good_count('goods.csv', 'new_goods.csv', 'beer')
