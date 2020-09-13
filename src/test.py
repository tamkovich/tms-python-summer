from datetime import date, timedelta, time


class Shift:
    time_from: time
    time_to: time
    date_from: date
    date_to: date
    week_days: list

    @staticmethod
    def compare(self, other):
        for day in self.week_days:
            if day in other.week_days:
                if self.date_from < other.date_to and self.date_to > other.date_from:
                    if self.time_from <= other.time_from <= self.time_to or self.time_from <= other.time_to <= self.time_to:
                        return 'пересекают'
                    if self.time_from > self.time_to or other.time_from > other.time_to:
                        if self.time_from < other.time_to or other.time_from < self.time_to:
                            return 'пересекают'
                        elif (self.time_from < other.time_from and self.time_to > other.time_to) or \
                                (other.time_from < self.time_from and self.time_to > other.time_to):
                            return 'пересекают'
        return 'не пересекают'


men1 = Shift()
men1.time_from = time(7, 00, 00)
men1.time_to = time(13, 00, 00)
men1.date_from = date(2020, 1, 1)
men1.date_to = date(2020, 1, 10)
men1.week_days = [1, 4, 3]

men2 = Shift()
men2.time_from = time(7, 0, 00)
men2.time_to = time(5, 0, 00)
men2.date_from = date(2020, 1, 1)
men2.date_to = date(2020, 1, 10)
men2.week_days = [1, 2, 6]

print(Shift.compare(men1, men2))
