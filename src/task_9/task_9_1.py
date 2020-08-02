"""
Дан список строк. Отформатировать все строки в формате ‘{i} - {string}’, где i
это порядковый номер строки в списке. Использовать генератор списков.
"""


list_of_strings = [
    "Python", "C++", "Java", "PHP", "Java Script", "C", "Ruby", "C#", "Pascal", "Delphi",
]

list_result = [f'{i} - {el}' for i, el in enumerate(list_of_strings)]
print(list_result)
