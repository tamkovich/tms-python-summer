"""
1. Создать класс Matrix.
2. Атрибуты - data(содержит саму матрицу - список списков), n, m.
3. Определить конструктор(с параметрами(передача размерности: n, m и диапазона случайных чисел: a, b),
по-умолчанию (матрица 5 на 5 где все элементы равны нулю), копирования) ,
4. Переопределить магический метод str для красивого вывода.
5. Описать функции, которые принимают на вход объект класса Matrix. Функции позволяют искать
максимальный элемент матрицы, минимальный, сумму всех элементов.
6. Создать в файле main.py матрицу. Воспользоваться всеми описанными функциями и методами
"""

from src.HW.matrix_utils import matrix_classes, matrix_funcs

if __name__ == '__main__':
    m1 = matrix_classes.Matrix()
    print(m1)

    m2 = matrix_classes.Matrix(3, 3, [-100, 100])
    print(m2)

    m3 = matrix_classes.Matrix(m2)
    print(m3)

    print(matrix_funcs.find_min_matrix_element(m2))
    print(matrix_funcs.find_max_matrix_element(m2))
    print(matrix_funcs.find_sum_matrix_elements(m2))
