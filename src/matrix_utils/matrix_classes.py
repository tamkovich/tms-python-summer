from random import randint


class Matrix:
    def __init__(self, n: int, m: int, a: int, b: int) -> None:
        self.n = n
        self.m = m
        self.a = a
        self.b = b
        self._data: list[list] = None

    @property
    def data(self):
        pass

    @data.setter
    def data(self, data):
        self._data = data

    def gen_default_matrix(self) -> None:
        """Сгенерировать матрицу по умолчанию (нулевую)"""
        self._data = [
            [randint(self.a, self.b) for _ in range(self.n)] for _ in range(self.m)
        ]
        return self._data

    def __str__(self) -> str:
        return f"your matrix is {self._data}"