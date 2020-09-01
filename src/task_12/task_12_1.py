"""
Создать класс MyTime. Атрибуты: hours, minutes, seconds. Методы:
переопределить магические методы сравнения(==, !=, >=, <=, <, >),
сложения, вычитания, умножения на число, вывод на экран. Перегрузить
конструктор на обработку входных параметров вида: одна строка, три
числа, другой объект класса MyTime, и отсутствие входных параметров.
Реализовать нормальное отображение времени(12:65:83 - 13:06:23)
"""


class MyTime:
    def __init__(self, hours: int, minutes: int, seconds: int) -> tuple:
        """
        convert time to good look
        :param hours: int
        :param minutes: int
        :param seconds: int
        return tuple (int, int, int)
        """
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        if self.seconds > 59:
            self.seconds -= 60 * (self.seconds // 60)
            self.minutes += self.seconds // 60
        if self.minutes > 59:
            self.minutes -= 60 * (self.minutes // 60)
            self.hours += self.minutes // 60
        if self.hours > 23:
            self.hours -= 24 * (self.hours // 24)

    def __eq__(self, other):
        return self.hours == other.hours and self.minutes == other.minutes and self.seconds == other.seconds

    def __ne__(self, other):
        return not self.hours == other.hours and self.minutes == other.minutes and self.seconds == other.seconds

    def __lt__(self, other):
        return (
                self.hours == other.hours and self.minutes == other.minutes and self.seconds < other.seconds or
                self.hours == other.hours and self.minutes < other.minutes or
                self.hours < other.hours
        )

    def __le__(self, other):
        return (
                self.hours == other.hours and self.minutes == other.minutes and self.seconds == other.seconds or
                self.hours == other.hours and self.minutes == other.minutes and self.seconds < other.seconds or
                self.hours == other.hours and self.minutes < other.minutes or
                self.hours < other.hours
        )

    def __gt__(self, other):
        return (
                self.hours == other.hours and self.minutes == other.minutes and self.seconds > other.seconds or
                self.hours == other.hours and self.minutes > other.minutes or
                self.hours > other.hours
        )

    def __ge__(self, other):
        return (
                self.hours == other.hours and self.minutes == other.minutes and self.seconds == other.seconds or
                self.hours == other.hours and self.minutes == other.minutes and self.seconds > other.seconds or
                self.hours == other.hours and self.minutes > other.minutes or
                self.hours > other.hours
        )

    def __add__(self, other):
        return self.hours + other.hours, self.minutes + other.minutes, self.seconds + other.seconds

    def __sub__(self, other):
        return abs(self.hours-other.hours), abs(self.minutes-other.minutes), abs(self.seconds-other.seconds)

    def __mul__(self, n):
        return self.hours * n, self.minutes * n, self.seconds * n

    def __str__(self):
        return f'{self.hours}:{self.minutes}:{self.seconds}'


class MyTimeString(MyTime):  # Входные данные: одна строка
    def __init__(self, string: input) -> tuple:
        """
        Дочерний класс MyTime.
        Принимает на вход строку, числа д.б. разделены двоеточием
        :param string: string
        """
        self.string = string.split(':')
        self.hours = int(self.string[0])
        self.minutes = int(self.string[1])
        self.seconds = int(self.string[2])

class MyTimeNumber(MyTime):   # Входные данные: 3 числа
    def __init__(self):
        """
        Дочерний класс MyTime.
        Принимает на вход три числа, введенных с клавиатуры
        """
        self.hours = int(input("hours:"))
        self.minutes = int(input("minutes:"))
        self.seconds = int(input("seconds:"))

class MyTimeMyTime(MyTime):   # Входные данные: др. обьект класса
    def __init__(self, anytime: MyTime):
        """
        Дочерний класс MyTime.
        Принимает на вход другой экземпляр этого же класса
        :param anytime: экземпляр класса MyTime
        """
        self.hours = anytime.hours
        self.minutes = anytime.minutes
        self.seconds = anytime.seconds

class MyTimeNone(MyTime):  # Входные данные: отсутствуют
    def __init__(self):
        """
        Дочерний класс MyTime.
        Принимает на вход ничего.
        """
        self.hours = None
        self.minutes = None
        self.seconds = None
