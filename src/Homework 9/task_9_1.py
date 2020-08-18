# task_9_1
"""
Дан список строк. Отформатировать все строки в формате {i}-{string}, где
i это порядковый номер строки в списке. Использовать генератор списков.
"""

list_of_string = [
    "apple", "berry", "banana", "lemon", "orange"
]

print([f"{i} - {element}" for i, element in enumerate(list_of_string)])
