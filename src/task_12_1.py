import datetime
class MyTime:
    def __init__(self,  hours, minutes, seconds):
        self.seconds = seconds
        if seconds > 59:
            add_min = seconds // 60
            seconds %= 60
            minutes += add_min
        self.minutes = minutes

        if minutes > 59:
            add_hours = minutes // 60
            minutes %= 60
            hours += add_hours
        self.hours = hours

        if hours > 23:
            hours %= 24


        self.whole_time = datetime.time(hours, minutes, seconds)

    def __eq__(self, other):
        return self.whole_time == other.whole_time
    def __ne__(self, other):
        return self.whole_time != other.whole_time
    def __lt__(self, other):
        return self.whole_time < other.whole_time
    def __gt__(self, other):
        return self.whole_time > other.whole_time
    def __le__(self, other):
        return self.whole_time <= other.whole_time
    def __ge__(self, other):
        return self.whole_time >= other.whole_time
    def __add__(self, other):
        sum1 = self.seconds + other.seconds
        if sum1 > 59:
            add_min = sum1 // 60
            sum1 %= 60
            self.minutes += add_min
        sum2 = self.minutes + other.minutes
        if sum2 > 59:
            add_hours = sum2 // 60
            sum2 %= 60
            self.hours += add_hours
        sum3 = self.hours + other.hours
        if sum3 > 23:
            sum3 %= 24


        return sum3, sum2, sum1
    def __mul__(self, other):
        prod1 = self.seconds * other
        if prod1 > 59:
            add_min = prod1 // 60
            prod1 %= 60
            self.minutes += add_min
        prod2 = self.minutes * other
        if prod2 > 59:
            add_hours = prod2// 60
            prod2 %= 60
            self.hours += add_hours
        prod3 = self.hours * other
        if prod3 > 23:
            prod3 %= 24
        return prod3, prod2, prod1
    def __repr__(self):
        return print(self.whole_time)









vremya = MyTime(112, 132, 122)
time1 = MyTime(12, 3, 43)
print(vremya.__eq__(time1))
print(vremya.__add__(time1))
vremya.__repr__()




