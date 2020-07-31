"""
В конец существующего текстового файла записать три новые строки текста.
Записываемые строки вводятся с клавиатуры.
"""

try:
    my_file = open('test.txt', 'a', encoding='utf8')
except FileNotFoundError:
    my_file = open('test.txt', 'w', encoding='utf8')

for i in range(3):
    my_file.write(input() + '\n')
