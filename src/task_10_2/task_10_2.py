"""
В конец существующего текстового файла записать три новые строки текста.
Записываемые строки вводятся с клавиатуры.
"""

with open('task_10_2.txt', 'a') as my_file:
    for _ in range(3):
        in_str = input('Enter string: ')
        my_file.write(f'{in_str}\n')
