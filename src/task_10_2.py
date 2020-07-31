"""
Создать текстовый файл и записать в него 6 строк. Записываемые строки вводятся с клавиатуры.
"""

my_file = open('test.txt', 'w', encoding='utf8')

for i in range(6):
    my_file.write(input() + '\n')
