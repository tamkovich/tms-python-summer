"""
Создать класс Matrix. Атрибуты - data(содержит саму матрицу - список
списков), n, m. Определить конструктор(с параметрами(передача размерности:
n, m и диапазона случайных чисел: a, b), по-умолчанию (матрица 5 на 5 где все
элементы равны нулю), копирования) ,переопределить магический метод str для
красивого вывода. Описать функции, которые принимают на вход объект класса
Matrix. Функции позволяют искать максимальный элемент матрицы, минимальный,
сумму всех элементов. Создать в файле main.py матрицу. Воспользоваться всеми
описанными функциями и методами
"""


from matrix_utils import matrix_classes
from matrix_utils import matrix_funcs

if __name__ == "__main__":
    mtrx = matrix_classes.Matrix(10, 50, 6, 6)
    print(mtrx)
    print(matrix_funcs.find_max_matrix_element(mtrx))
    print(matrix_funcs.find_min_matrix_element(mtrx))
    print(matrix_funcs.find_sum_matrix_elements(mtrx))
    mtrx.gen_default_matrix()
    print(mtrx)
