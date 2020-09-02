"""
Создать класс MyTime. Атрибуты: hours, minutes, seconds. Методы:
переопределить магические методы сравнения(==, !=, >=, <=, <, >),
сложения, вычитания, умножения на число, вывод на экран. Перегрузить
конструктор на обработку входных параметров вида: одна строка, три
числа, другой объект класса MyTime, и отсутствие входных параметров.
Реализовать нормальное отображение времени(12:65:83 - 13:06:23)
"""


class MyTime:
    def __init__(self, *args):
        self.hours = args[0]
        self.minutes = args[1]
        self.seconds = args[2]
        self.days = 0
        while self.seconds >= 60:
            self.minutes += 1
            self.seconds -= 60
        while self.minutes >= 60:
            self.hours += 1
            self.minutes -= 60
        while self.hours > 24:
            self.days += 1
            self.hours -= 24

    def __eq__(self, other):
        return self.hours == other.hours and self.minutes == other.minutes and self.seconds == other.seconds

    def __lt__(self, other):
        if self.hours > other.hours:
            return False
        elif self.hours < other.hours:
            return True
        elif self.hours == other.hours and self.minutes > other.minutes:
            return False
        elif self.hours == other.hours and self.minutes < other.minutes:
            return True
        elif self.hours == other.hours and self.minutes == other.minutes and self.seconds > other.seconds:
            return False
        elif self.hours == other.hours and self.minutes == other.minutes and self.seconds < other.seconds:
            return True
        elif self.hours == other.hours and self.minutes == other.minutes and self.seconds == other.seconds:
            return False

    def __le__(self, other):
        if self.hours > other.hours:
            return False
        elif self.hours < other.hours:
            return True
        elif self.hours == other.hours and self.minutes > other.minutes:
            return False
        elif self.hours == other.hours and self.minutes < other.minutes:
            return True
        elif self.hours == other.hours and self.minutes == other.minutes and self.seconds > other.seconds:
            return False
        elif self.hours == other.hours and self.minutes == other.minutes and self.seconds < other.seconds:
            return True
        elif self.hours == other.hours and self.minutes == other.minutes and self.seconds == other.seconds:
            return True

    def __add__(self, other):
        self.seconds += other.seconds
        self.minutes += other.minutes
        self.hours += other.hours
        while self.seconds > 60:
            self.minutes += 1
            self.seconds -= 60
        while self.minutes > 60:
            self.hours += 1
            self.minutes -= 60
        while self.hours > 24:
            self.days += 1
            self.hours -= 24
        return self.days, self.hours, self.minutes, self.seconds

    def __sub__(self, other):
        self.seconds -= other.seconds
        self.minutes -= other.minutes
        self.hours -= other.hours
        while self.seconds < 0:
            self.minutes -= 1
            self.seconds += 60
        while self.minutes < 0:
            self.hours -= 1
            self.minutes += 60
        while self.hours < 0:
            self.days -= 1
            self.hours += 24
        return self.days, self.hours, self.minutes, self.seconds

    def __mul__(self, other):
        self.seconds *= other.seconds
        self.minutes *= other.minutes
        self.hours *= other.hours
        while self.seconds >= 60:
            self.minutes += 1
            self.seconds -= 60
        while self.minutes >= 60:
            self.hours += 1
            self.minutes -= 60
        while self.hours > 24:
            self.days += 1
            self.hours -= 24
        return self.days, self.hours, self.minutes, self.seconds

    def __repr__(self):
        return str(f'{self.days} days - {self.hours}:{self.minutes}:{self.seconds}')


time = MyTime(1, 2, 3)
time1 = MyTime(1, 59, 59)

print(time)
