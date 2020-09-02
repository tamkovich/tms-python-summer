"""
Написать функции по работе с csv файлами в файле csv_utils.py.
Чтение. Запись. Добавление записи(по позиции, по-умолчанию в конец).
Удаление записи(по позиции, по-умолчанию последнюю).
В файле task_10_08 импортировать функции.
С помощью функций создать файл с информацией о
товарах(Имя товара, цена, количество, комментарий).
Прочесть файл, Добавить новую позицию в конец. Удалить третью строку.
"""

import csv_utils

csv_utils.csv_writer([
    ['product name', 'price', 'quantity', 'comment'],
    ['car', '342', '6', 'fsdgjrtyj'],
    ['mr.bean', '2222', '1', 'sdasda'],
    ['dfsf', '4545', '8786', 'jghdjdkhjg'],
    ['mr.sadwer', '5647', '5', 'hfnfgjsdgf'],
    ['fdsfmrnm', '7856', '65', '1242134erger'],
    ['mr.bean', '2222', '1', 'sdasda'],
], 'test_csv.csv')
# csv_utils.csv_position_write('Liverpool', 'test_csv.csv', 3)
#

test = csv_utils.csv_read('test_csv.csv')
print(test)
csv_utils.csv_position_write(['car', '342', '6', 'fsdgjrtyj'], 'test_csv.csv')
csv_utils.csv_position_delete('test_csv.csv', 2)

