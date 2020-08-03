# Дан список строк. Отформатировать все строки в формате ‘{i} - {string}’, где i
# это порядковый номер строки в списке. Использовать генератор списков.

strings = ['none', 'str2', 'dump']

res = [f'{i} - {elem}' for i, elem in enumerate(strings)]

print(res)
