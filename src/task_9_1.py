#  Дан список строк. Отформатировать все строки в формате ‘{i} - {string}’, где i
# это порядковый номер строки в списке. Использовать генератор списков.
spisok_strok = [ 27, 'kek', 1995, 'lol']
print((lambda string:
       [f'{index} - {value}' for index, value in enumerate(string)])
      (spisok_strok))