import datetime


class MyTime:
    def __init__(self, hours=None, minuts=None, seconds=None):
        self.hours = hours
        self.minuts = minuts
        self.seconds = seconds

        if self.seconds > 59:
            self.seconds -= 60 * (self.seconds // 60)
            self.minuts += 1 * (self.seconds // 60)
        if self.minuts > 59:
            self.minuts -= 60 * (self.minuts // 60)
            self.hours += 1 * (self.minuts // 60)
        if self.hours > 23:
            self.hours -= 24 * (self.hours // 24)
        self.time = datetime.time(hour=self.hours, minute=self.minuts, second=self.seconds)

    def __lt__(self, other):
        return self.time < other.time

    def __le__(self, other):
        return self.time <= other.time

    def __eq__(self, other):
        return self.time == other.time

    def __ne__(self, other):
        return self.time != other.time

    def __gt__(self, other):
        return self.time > other.time

    def __ge__(self, other):
        return self.time >= other.time

    def __add__(self, other):
        time_1 = datetime.timedelta(hours=self.hours, minutes=self.minuts, seconds=self.seconds)
        time_2 = datetime.timedelta(hours=other.hours, minutes=other.minuts, seconds=other.seconds)
        return time_1 + time_2

    def __sub__(self, other):
        time_1 = datetime.timedelta(hours=self.hours, minutes=self.minuts, seconds=self.seconds)
        time_2 = datetime.timedelta(hours=other.hours, minutes=other.minuts, seconds=other.seconds)
        return time_1 - time_2

    def __mul__(self, num=1):
        time_1 = datetime.timedelta(hours=self.hours, minutes=self.minuts, seconds=self.seconds)
        return time_1 * num

    def vizov(self):
        return self.time


class MyTime_string(MyTime):
    def __init__(self, string):
        spis = string.split(':')
        self.hours = int(spis[0])
        self.minuts = int(spis[1])
        self.seconds = int(spis[2])

        if self.seconds > 59:
            self.seconds -= 60 * (self.seconds // 60)
            self.minuts += 1 * (self.seconds // 60)
        if self.minuts > 59:
            self.minuts -= 60 * (self.minuts // 60)
            self.hours += 1 * (self.minuts // 60)
        if self.hours > 23:
            self.hours -= 24 * (self.hours // 24)
        self.time = datetime.time(hour=self.hours, minute=self.minuts, second=self.seconds)


class MyTime_time(MyTime):
    def __init__(self, my_time):
        self.hours = my_time.hours
        self.minuts = my_time.minuts
        self.seconds = my_time.seconds
        self.time = my_time.time


class MyTime_None(MyTime):
    def __init__(self):
        self.hours = 0
        self.minuts = 0
        self.seconds = 0
        self.time = datetime.time(hour=self.hours, minute=self.minuts, second=self.seconds)


time1 = MyTime(10, 10, 10)
time2 = MyTime_string('20:15:20')
x = time1
time3 = MyTime_time(x)
time4 = MyTime_None()


print(f'res = {time3 + time2}')
print(f'res = {time1 - time4}')
print(f'res = {time1 * 3}')
