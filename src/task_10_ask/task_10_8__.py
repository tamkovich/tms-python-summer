"""
Написать функции по работе с csv файлами в файле csv_utils.py. Чтение.
Запись. Добавление записи(по позиции, по-умолчанию в конец). Удаление
записи(по позиции, по-умолчанию последнюю).
В файле task_10_08 импортировать функции. С помощью функций создать
файл с информацией о товарах(Имя товара, цена, количество,
комментарий).
Прочесть файл, Добавить новую позицию в конец. Удалить третью строку.
"""
# import csv
import csv_utils


# rows = [
#     ['product name', 'product price', 'count prod', 'comments'],
#     ['food', '100', '600', "good"],
#     ['boals', '345', '100', 'better'],
#     ['soks', '20', '300', 'low'],
#     ['tiger', '1000', '1', 'best'],
# ]
# filename = 'infoprod.csv'
# with open(filename, 'w') as csvfile:
#     csvwriter = csv.writer(csvfile)
#     csvwriter.writerows(rows)
csv_utils.csv_writer = ([
    ['product name', 'product price', 'count prod', 'comments'],
    ['food', '100', '600', "good"],
    ['boals', '345', '100', 'better'],
    ['soks', '20', '300', 'low'],
    ['tiger', '1000', '1', 'best'],
], 'info.csv')
test = csv_utils.csv_reader('info.csv')
print(test)
# info = csv_utils.csv_reader('info_csv.csv')
# print(info)


# with open(filename, 'w') as csvfile:
#     csvwriter = csv.writer(csvfile)
#     csvwriter.writerows(rows)
