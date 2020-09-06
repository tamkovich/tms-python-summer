"""
Создать класс Matrix.
Атрибуты - data(содержит саму матрицу - список списков), n, m.
Определить конструктор(с параметрами(передача размерности: n, m
и диапазона случайных чисел: a, b), по-умолчанию
(матрица 5 на 5 где все элементы равны нулю), копирования) ,
переопределить магический метод str для красивого вывода.
Описать функции, которые принимают на вход объект класса Matrix.
 Функции позволяют искать максимальный элемент матрицы, минимальный,
 сумму всех элементов.
Создать в файле main.py матрицу.
Воспользоваться всеми описанными функциями и методам
"""


from matrix_utils.matrix_classes import Matrix
from matrix_utils import matrix_funcs


if __name__ == "__main__":
    matrix = Matrix(5, 5, 11, 33)
    matrix.gen_default_matrix()
    print(matrix)
    print(matrix_funcs.find_max_matrix_element(matrix))
    print(matrix_funcs.find_min_matrix_element(matrix))
    print(matrix_funcs.find_sum_matrix_elements(matrix))
