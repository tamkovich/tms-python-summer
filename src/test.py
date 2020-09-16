from datetime import date, timedelta, time


class Shift:
    def __init__(self,
                 time_from: time,
                 time_to: time,
                 date_from: date,
                 date_to: date,
                 week_days: list):
        self.time_from = time_from
        self.time_to = time_to
        self.date_from = date_from
        self.date_to = date_to
        self.week_days = week_days

    @staticmethod
    def compare(self, other):
        date_from = timedelta(hours=self.time_from.hour,
                              minutes=self.time_from.minute,
                              seconds=self.time_from.second)
        date_to = timedelta(hours=self.time_to.hour,
                            minutes=self.time_to.minute,
                            seconds=self.time_to.second)

        other_date_from = timedelta(hours=other.time_from.hour,
                                    minutes=other.time_from.minute,
                                    seconds=other.time_from.second)
        other_date_to = timedelta(hours=other.time_to.hour,
                                  minutes=other.time_to.minute,
                                  seconds=other.time_to.second)
        for day in tuple(self.week_days):
            if (timedelta(hours=24) - date_from) < date_to:
                if not (day + 1 in self.week_days):
                    self.week_days.append(day + 1)
                    self.date_to = self.date_to + timedelta(days=1)
        for day in tuple(other.week_days):
            if (timedelta(hours=24) - other_date_from) < other_date_to:
                if not (day + 1 in other.week_days):
                    other.week_days.append(day + 1)
        for day in self.week_days:
            if day in other.week_days:
                if self.date_from <= other.date_from <= self.date_to or \
                        other.date_from <= self.date_from <= other.date_to:
                    if self.time_from <= other.time_from < self.time_to or \
                            self.time_from <= other.time_to < self.time_to:
                        return True
                    if self.time_from > self.time_to or other.time_from > other.time_to:
                        if self.time_from < other.time_to or other.time_from < self.time_to:
                            return True
        return False
