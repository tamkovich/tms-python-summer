"""
Создать класс MyTime. Атрибуты: hours, minutes, seconds. Методы:
переопределить магические методы сравнения(==, !=, >=, <=, <, >),
сложения, вычитания, умножения на число, вывод на экран. Перегрузить
конструктор на обработку входных параметров вида: одна строка, три
числа, другой объект класса MyTime, и отсутствие входных параметров.
Реализовать нормальное отображение времени(12:65:83 - 13:06:23)
"""


class MyTime:
    def __init__(self, hours, minutes, seconds):
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


# time = MyTime(10, 10, 15)
# time1 = MyTime(10, 10, 15)
# print(time == time1)
# print(time != time1)
# time2 = MyTime(10, 10, 11)
# print(time.__gt__(time2))
# print(time.__add__(time1))
# print(time.__sub__(time2))
# print(time.__mul__(3))
# print(time.__str__())
# print(dir(MyTime))
# print(time.hours)

class MyTimeString(MyTime):  # Входные данные: одна строка
    def __init__(self, string):
        self.string = string.split(':')
        self.hours = int(self.string[0])
        self.minutes = int(self.string[1])
        self.seconds = int(self.string[2])

class MyTimeNumber(MyTime):   # Входные данные: 3 числа
    def __init__(self):
        self.hours = int(input("hours:"))
        self.minutes = int(input("minutes:"))
        self.seconds = int(input("seconds:"))

class MyTimeMyTime(MyTime):   # Входные данные: др. обьект класса
    def __init__(self, anytime):
        self.hours = anytime.hours
        self.minutes = anytime.minutes
        self.seconds = anytime.seconds

class MyTimeNone(MyTime):  # Входные данные: отсутствуют
    def __init__(self):
        self.hours = None
        self.minutes = None
        self.seconds = None


# time4 = MyTimeString('12:38:15')
# print(time4.__str__())
# print(time.__sub__(time4))
# time5 = MyTimeNumber()
# print(time5.__str__())
# print(time.__sub__(time5))
# timeX = MyTime(43, 67, 80)
# print(timeX.__str__())
# timeM = MyTimeMyTime(time5)
# print(timeM.__str__())
# timeN = MyTimeNone
# print(timeN.__dict__)
