"""Создать класс Book. Атрибуты: количество страниц, год издания,
автор, цена. Добавить валидацию в конструкторе на
ввод корректных данных. Создать иерархию ошибок."""


class CountPagesException(Exception):
    def __init__(self, page_count, message="Page count must be positive integer value"):
        self.__page_count = page_count
        self.__message = message
        super().__init__(message)

    def __str__(self):
        return f'{self.__page_count} -> {self.__message}'


class Book:
    page_count: int
    year: int
    author: str
    price: int

    def __init__(self, page_count, year, author, price):
        if page_count > 0 and type(page_count) == int:
            self.page_count = page_count
        else:
            raise CountPagesException(page_count)

        self.year = year
        self.author = author
        self.price = price


# testing
if __name__ == '__main__':
    b = Book(0, 1990, 'Somebody', 200)
