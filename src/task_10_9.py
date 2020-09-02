"""
Использовать результаты 10.8. Все функции описываются в csv_utils.py.
Проверка работы функции осуществляется в task_10_09.py.
1) Создать функцию подсчета полной суммы всех товаров.
2) Создать функцию поиска самого дорогого товара.
3) Создать функцию самого дешевого товара.
4) Создать функцию уменьшения количества товара(на n, по-умолчанию на 1)
"""

from task_10 import csv_utils

print(csv_utils.csv_sum_price('test_csv.csv'))
print(csv_utils.search_max_price('test_csv.csv'))
print(csv_utils.search_min_price('test_csv.csv'))
csv_utils.decrease_quantity('test_csv.csv')
