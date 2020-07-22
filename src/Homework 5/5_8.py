# task_5_8
"""В заданной строке расположить в обратном порядке все слова. Разделителями
слов считаются пробелы."""

text = input("Enter some string: ")

for i in text.split(" "):
    print(i[::-1], end=" ")
