# task_13
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
    matrix = matrix_classes.Matrix(1, 10, 3, 3)

    print(matrix)
    print(matrix_funcs.sum_of_elements(matrix))
    print(matrix_funcs.max_element(matrix))
    print(matrix_funcs.min_element(matrix))

    matrix.gen_default_matrix()
    print(matrix)
