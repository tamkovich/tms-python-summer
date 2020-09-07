import time
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

class Timer(MyTime):
    def __init__(self, time_input: str = '0:0:0') -> (int, int, int):
        """
        класс, переводящий время из строки в три числа
        :param time_input: время - строка из трех чисел, разделенных ':'
        """
        self.time_input = time_input.split(':')
        for i, el in enumerate(self.time_input):
            if len(el) > 2:
                raise SyntaxError('len input digit must be 1 or 2 element')
            if not el.isdigit():
                raise ValueError("input must be integer")
        self.hours = int(self.time_input[0])
        self.minutes = int(self.time_input[1])
        self.seconds = int(self.time_input[2])

    def countdown_time(self):
        sec = self.seconds + self.minutes * 60 + self.hours * 3600
        while sec > 1:
            sec -= 1
            time.sleep(1)
            s = sec % 60
            m = (sec // 60) % 60
            h = sec // 3600
            output = f'{Timer.__getForm(h)}:' \
                     f'{Timer.__getForm(m)}:' \
                     f'{Timer.__getForm(s)}'
            print(output)
            if sec == 1:
                break
        return 'ALARM!!!'

    @staticmethod
    def __getForm(x):
        return str(x) if x > 9 else '0' + str(x)
