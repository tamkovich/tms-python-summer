"""Создать класс MyTime. Атрибуты: hours, minutes, seconds. Методы:
переопределить магические методы сравнения(==, !=, >=, <=, <, >),
сложения, вычитания, умножения на число, вывод на экран. Перегрузить
конструктор на обработку входных параметров вида: одна строка, три
числа, другой объект класса MyTime, и отсутствие входных параметров.
Реализовать нормальное отображение времени(​ 12:65:83​ - 13:06:23)
[my-oop-02] ​ Задание доделать в рамках cw12
Примечание: http://sheregeda.github.io/blog/2015/01/18/maghichieskiie-mietody-python/"""


class MyTime:
    def __init__(self, *args):
        # Here setters are invoked for checking valid values
        arg_len = len(args)
        if arg_len == 0:
            self.hours = 0
            self.minutes = 0
            self.seconds = 0
        elif arg_len == 3:
            self.hours = args[0]
            self.minutes = args[1]
            self.seconds = args[2]
        elif arg_len == 1 and type(args[0]) == str:
            h, m, s = args[0].split(':')
            self.hours = int(h)
            self.minutes = int(m)
            self.seconds = int(s)
        elif arg_len == 1 and type(args[0]) == MyTime:
            self.hours = args[0].hours
            self.minutes = args[0].minutes
            self.seconds = args[0].seconds
        else:
            raise Exception('Invalid data: incorrect number of parameters')

    def __eq__(self, other):
        return self.__hours * 3600 + self.__minutes * 60 + self.__seconds == \
               other.__hours * 3600 + other.__minutes * 60 + other.__seconds

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        return self.__hours * 3600 + self.__minutes * 60 + self.__seconds > \
               other.__hours * 3600 + other.__minutes * 60 + other.__seconds

    def __lt__(self, other):
        return self.__hours * 3600 + self.__minutes * 60 + self.__seconds < \
               other.__hours * 3600 + other.__minutes * 60 + other.__seconds

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __add__(self, other):
        full_seconds = (self.__hours + other.__hours) * 3600 + \
                       (self.__minutes + other.__minutes) * 60 + \
                       self.__seconds + other.__seconds

        h = full_seconds // 3600
        m = (full_seconds % 3600) // 60
        s = (full_seconds % 3600) % 60

        return MyTime(h, m, s)

    def __sub__(self, other):
        full_seconds = (self.__hours - other.__hours) * 3600 + \
                       (self.__minutes - other.__minutes) * 60 + \
                       self.__seconds - other.__seconds

        h = full_seconds // 3600
        m = (full_seconds % 3600) // 60
        s = (full_seconds % 3600) % 60

        return MyTime(h, m, s)

    def __rmul__(self, other):
        full_seconds = other * (self.__hours * 3600 + self.__minutes * 60 + self.__seconds)

        h = full_seconds // 3600
        m = (full_seconds % 3600) // 60
        s = (full_seconds % 3600) % 60

        return MyTime(h, m, s)

    def __mul__(self, other):
        return self.__rmul__(other)

    def __repr__(self):
        return f'h:m:s {self.__hours}:{self.__minutes}:{self.__seconds}'

    @property
    def hours(self):
        return self.__hours

    @hours.setter
    def hours(self, hours):
        if type(hours) == int and (0 <= hours <= 23):
            self.__hours = hours
        else:
            raise Exception('hours: Invalid data')

    @property
    def minutes(self):
        return self.__minutes

    @minutes.setter
    def minutes(self, minutes):
        if type(minutes) == int and (0 <= minutes <= 59):
            self.__minutes = minutes
        else:
            raise Exception('minutes: Invalid data')

    @property
    def seconds(self):
        return self.__seconds

    @seconds.setter
    def seconds(self, seconds):
        if type(seconds) == int and (0 <= seconds <= 59):
            self.__seconds = seconds
        else:
            raise Exception('seconds: Invalid data')


# testing
if __name__ == '__main__':
    t1 = MyTime(4, 56, 59)
    t2 = MyTime(4, 24, 30)
    t3 = t1
    print(t1 == t2)
    print(t1 != t2)
    print(t1 > t2)

    print(t1 < t2)
    print(t1 < t3)
    print(t1)
    print(t3)

    t3.hours = 1
    print(t1)
    print(t3)

    t4 = t1 + t2
    print(t4)
    print('--------------------')

    t1 = MyTime(12, 34, 23)
    t2 = MyTime(10, 45, 3)
    t3 = t1 + t2
    print(f't1 + t2 = {t3}')

    print(t2 >= t1)
    t4 = t1 - t2
    print(f't1 - t2 = {t4}')

    t5 = MyTime(t4)
    print(t5)

    t6 = MyTime('12:34:9')
    print(t6)

    t6 = MyTime()
    print(t6)

    t6 = 2 * t4
    print(t6)

    t6 = t4 * 2
    print(t6)
