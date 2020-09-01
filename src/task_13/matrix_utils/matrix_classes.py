import random as r
import numpy as np


class Matrix:

    def __init__(self, a: int, b: int, n: int = 5, m: int = 5) -> list:
        """
        matrix
        :param n: количество рядов (по умолчанию 5)
        :param m: количество столбцов (по умолчанию 5)
        :param a: крайнее значение диапазона
        :param b: второе крайнее значение диапазона
        """
        self.n = n
        self.m = m
        self._a = a
        self._b = b
        self._data = [
            [r.randint(min(self._a, self._b), max(self._a, self._b))
             for _ in range(self.n)]
            for _ in range(self.m)
        ]

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    def gen_default_matrix(self) -> list:
        """Сгенерировать матрицу по умолчанию (нулевую)"""
        self._data = [[0 for _ in range(self.n)] for _ in range(self.m)]
        return self._data

    def __str__(self) -> str:
        """Make look matrix beauty"""
        return str(np.array(self._data))
