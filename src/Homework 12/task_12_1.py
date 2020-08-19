# task_12_1
"""Создать класс MyTime. Атрибуты: hours, minutes, seconds. Методы:
переопределить магические методы сравнения(==, !=, >=, <=, <, >),
сложения, вычитания, умножения на число, вывод на экран. Перегрузить
конструктор на обработку входных параметров вида: одна строка, три
числа, другой объект класса MyTime, и отсутствие входных параметров.
Реализовать нормальное отображение времени(12:65:83 - 13:06:23)"""
from typing import Tuple


def make_format(h: int, m: int, s: int) -> Tuple[int, int, int]:
    """
    Converts time to correct format
    :param h: hours
    :param m: minutes
    :param s: seconds
    :return: time in correct format
    """
    while s > 60:
        s -= 60
        m += 1
    while m > 60:
        m -= 60
        h += 1
    while h > 24:
        h -= 24
    return h, m, s


class MyTime:
    """
    Class allows you to work with time
    """

    def __init__(self, hours=3, minutes=34, seconds=21):
        """
        Constructor with class attributes
        :param hours: hours
        :param minutes: minutes
        :param seconds: seconds
        """
        hours: int
        minutes: int
        seconds: int
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __eq__(self, other) -> bool:
        """
        Compare two times (==)
        :param other: 2nd time
        :return: true if =, false if !=
        """
        return (
            self.hours == other.hours
            and self.minutes == other.minutes
            and self.seconds == other.seconds
        )

    def __ne__(self, other) -> bool:
        """
        Compare two times (!=)
        :param other: 2nd time
        :return: true if !=, false if ==
        """
        return not self.__eq__(other)

    def __ge__(self, other) -> bool:
        """
        Compare two times (>=)
        :param other: 2nd time
        :return: true if >=, false if <
        """

        if self.hours > other.hours:
            return True
        elif self.hours == other.hours:

            if self.minutes > other.minutes:
                return True
            elif self.minutes == other.minutes:

                if self.seconds >= other.seconds:
                    return True
                else:
                    return False

            else:
                return False

        else:
            return False

    def __le__(self, other) -> bool:
        """
        Compare two times (<=)
        :param other: 2nd time
        :return: true if <=, false if >
        """
        if self.hours < other.hours:
            return True
        elif self.hours == other.hours:

            if self.minutes < other.minutes:
                return True
            elif self.minutes == other.minutes:

                if self.seconds <= other.seconds:
                    return True
                else:
                    return False

            else:
                return False

        else:
            return False

    def __gt__(self, other) -> bool:
        """
        Compare two times (>)
        :param other: 2nd time
        :return: true if >, false if <=
        """
        if self.hours > other.hours:
            return True
        elif self.hours == other.hours:

            if self.minutes > other.minutes:
                return True
            elif self.minutes == other.minutes:

                if self.seconds > other.seconds:
                    return True
                else:
                    return False

            else:
                return False

        else:
            return False

    def __lt__(self, other) -> bool:
        """
        Compare two times (<)
        :param other: 2nd time
        :return: true if <, false if >=
        """
        if self.hours < other.hours:
            return True
        elif self.hours == other.hours:

            if self.minutes < other.minutes:
                return True
            elif self.minutes == other.minutes:

                if self.seconds < other.seconds:
                    return True
                else:
                    return False

            else:
                return False

        else:
            return False

    def __add__(self, other):
        """
        Sum two times (+)
        :param other: 2nd time
        :return: sum of two times
        """
        h = self.hours + other.hours
        m = self.minutes + other.minutes
        s = self.seconds + other.seconds
        h, m, s = make_format(h, m, s)
        return f"{h}:{m}:{s}"

    def __sub__(self, other):
        """
        Difference in two times (-)
        :param other: 2nd time
        :return: sub of two times
        """
        h = self.hours - other.hours
        m = self.minutes - other.minutes
        s = self.seconds - other.seconds
        h, m, s = make_format(h, m, s)
        return f"{h}:{m}:{s}"

    def __mul__(self, other):
        """
        Multiplication of time by number (*)
        :param other: 2nd time
        :return: mult of time and number
        """
        h = self.hours * other.hours
        m = self.minutes * other.minutes
        s = self.seconds * other.seconds
        h, m, s = make_format(h, m, s)
        return f"{h}:{m}:{s}"

    def __repr__(self):
        """
        Print time in correct format
        :return: print
        """
        return f"{self.hours}:{self.minutes}:{self.seconds}"


class MyTime2(MyTime):
    """
    Class whose constructor contains a string as parameters
    """

    def __init__(self, time: str):
        """
        Constructor with class attributes
        :param time: string which consists of (hours minutes seconds)
        """
        list_of_time = time.split()
        self.hours = int(list_of_time[0])
        self.minutes = int(list_of_time[1])
        self.seconds = int(list_of_time[2])
