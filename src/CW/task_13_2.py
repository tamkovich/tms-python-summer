"""Создать статичный метод add_numbers для класса Math. Метод возвращает сумму двух переданных чисел."""


class Math:
    __pi = 3.14

    def __init__(self):
        self.__a = 5

    @staticmethod
    def add_numbers(x, y):
        Math.__pi = 2
        return x + y

    def a(self):
        print(Math.__pi)


# testing
if __name__ == '__main__':
    m = Math()
    m.a()
    print(Math.add_numbers(3, 5))
    m.a()
    Math.add_numbers(2,3)
