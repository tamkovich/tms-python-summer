"""
В заданной строке расположить в обратном порядке все слова. Разделителями
слов считаются пробелы.
"""
strok_1 = str(input("some stroke: "))

strok_revers = ' '.join(strok_1.split(' ')[::-1])
print(f'output: {strok_revers}')
