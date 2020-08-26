import random
from typing import List
import numpy as np


class Matrix:
    """
    Allows to work with a matrix
    """

    def __init__(self, a: int, b: int, n: int = 5, m: int = 5):
        """
        Matrix attributes
        :param n: number of lines
        :param m: number of columns
        :param a: lower range for random
        :param b: higher range for random
        """
        self.b = b
        self.a = a
        self.n = n
        self.m = m
        self._data: List[list] = [[random.randint(a, b) for _ in range(self.n)] for _ in range(self.m)]

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    def gen_default_matrix(self) -> None:
        """
        Generate default matrix
        :return: nothing
        """
        self._data = np.zeros((self.n, self.m), dtype='int')

    def __str__(self) -> str:
        """
        Make the matrix look nice
        :return: some strings
        """
        some_str = ""
        for _ in self._data:
            some_str += f"{_}\n"
        return some_str
