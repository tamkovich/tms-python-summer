# task_10_8
"""В файле task_10_08 импортировать функции из csv_utils. С помощью функций
создать файл с информацией о товарах(Имя товара, цена, количество,
комментарий).
Прочесть файл, Добавить новую позицию в конец. Удалить третью строку."""

from csv_utils import *

size = input("Enter the number of products: ")

try:
    size = int(size)
except ValueError:
    print("Not a number")

list_of_product = [header := ["name", "price", "quantity", "comment"]]
length = len(header)

for i in range(size):
    line = []
    print(f"{i + 1} product:")
    for j in range(length):
        word = input(f"Enter {header[j]}: ")
        line.append(word)
    print()
    list_of_product.append(line)

path = "task_10_8.csv"
csv_write(path, "w", list_of_product)
list_of_product = csv_read(path, "r")

csv_append(path, ["chocolate", "100", "100", "tmp"], -1)
csv_delete(path, 2)
