from random import randint


class Matrix:
    def __init__(self, n: int = 5, m: int = 5, a: int = 0, b: int = 0) -> None:
        self.n = n
        self.m = m
        self.a = a
        self.b = b
        self._data: list[list] = [[randint(a, b) for _ in range(self.n)] for _ in range(self.m)]

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    def gen_default_matrix(self) -> None:
        """Сгенерировать матрицу по умолчанию (нулевую)"""
        self._data = [[0 for _ in range(self.n)] for _ in range(self.m)]

    def __str__(self) -> str:
        if self._data is None:
            return 'None'
        tmp = ""
        for i in self._data:
            tmp += f'{i}\n'
        return tmp

