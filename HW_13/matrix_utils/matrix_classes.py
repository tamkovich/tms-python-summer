from random import randint


class Matrix:
    def __init__(self, n: int = 5, m: int = 5, a: int = 0, b: int = 0):
        self.n = n
        self.m = m
        self.a = a
        self.b = b
        self.data = None

    def gen_default_matrix(self):
        self.data = [[randint(self.a, self.b) for j in range(self.n)] for i in range(self.m)]
        return self.data

    def __str__(self) -> str:
        return f'Matrix: {self.data}'
