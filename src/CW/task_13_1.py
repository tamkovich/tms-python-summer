"""Создать метод класса get_counter. Создать три объекта класса. Вызвать через класс метод get_counter."""


class Count:
    __COUNTER = 0

    def __init__(self):
        Count.__COUNTER += 1
        self.__a = 9

    @classmethod
    def get_counter(cls):
        print(Count.__COUNTER)

    @classmethod
    def add(cls, x, y):
        print(x + y)


# testing
if __name__ == '__main__':
    c1 = Count()
    c2 = Count()
    c3 = Count()
    Count.get_counter()
    c2.get_counter()
    Count.add(2, 3)
    c2.add(3, 2)
