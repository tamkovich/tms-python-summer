# В конец существующего текстового файла записать три новые строки текста.
# Записываемые строки вводятся с клавиатуры

with open('test.txt', 'a') as my_f:
    h = input()
    b = input()
    c = input()
    my_f.writelines(['\n', h,'\n', b,'\n', c])