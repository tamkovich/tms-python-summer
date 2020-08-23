# Дан список строк. Отформатировать все строки в формате ‘{i} - {string}’, где i
# это порядковый номер строки в списке. Использовать генератор списков.


random_list = [i for i in range(67, 74)]
print(random_list)
print((lambda string:
       [f'{index} - {value}' for index, value in enumerate(string)])
      (random_list))
