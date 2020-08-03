# task_10_9
"""Использовать результаты 10.8. Все функции описываются в csv_utils.py.
Проверка работы функции осуществляется в task_10_09.py.
Создать функцию подсчета полной суммы всех товаров.
Создать функцию поиска самого дорогого товара.
Создать функцию самого дешевого товара.
Создать функцию уменьшения количества товара(на n, по-умолчанию на 1)"""
import csv_utils

print("Total sum of all prices of products: ")
print(csv_utils.sum_of_price("task_10_8.csv"))

print("\nThe most expensive product: ")
print(csv_utils.search("task_10_8.csv", "max"))

print("\nThe cheapest product: ")
print(csv_utils.search("task_10_8.csv", "min"))

if csv_utils.purchase_of_product("task_10_8.csv", 10, "milk"):
    print("\nCheck file")
else:
    print("\nError")


