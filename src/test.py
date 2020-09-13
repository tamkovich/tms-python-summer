from datetime import date, timedelta, time, datetime


class Shift:
    def __init__(self):
        self.time_from: time
        self.time_to: time
        self.date_from: date
        self.date_to: date
        self.week_days: list

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
                        return 'пересекают'
                    if self.time_from > self.time_to or other.time_from > other.time_to:
                        if self.time_from < other.time_to or other.time_from < self.time_to:
                            return 'пересекают'
        return 'не пересекают'


tests_ok = [
    (
        dict(
            time_from=time(22, 00, 00),
            time_to=time(10, 00, 00),
            date_from=date(2020, 9, 1),
            date_to=date(2020, 9, 30),
            week_days=[2, 4],
        ),
        dict(
            time_from=time(8, 00, 00),
            time_to=time(17, 00, 00),
            date_from=date(2020, 9, 1),
            date_to=date(2020, 9, 30),
            week_days=[1, 3],
        ),
    ),
    (
        dict(
            time_from=time(8, 00, 00),
            time_to=time(5, 00, 00),
            date_from=date(2020, 1, 1),
            date_to=date(2020, 1, 10),
            week_days=[1, 2, 3],
        ),
        dict(
            time_from=time(10, 00, 00),
            time_to=time(13, 00, 00),
            date_from=date(2020, 1, 1),
            date_to=date(2020, 1, 10),
            week_days=[1, 2, 3],
        ),
    ),
    (
        dict(
            time_from=time(8, 00, 00),
            time_to=time(15, 00, 00),
            date_from=date(2020, 1, 1),
            date_to=date(2020, 1, 10),
            week_days=[1, 2, 3],
        ),
        dict(
            time_from=time(8, 00, 00),
            time_to=time(15, 00, 00),
            date_from=date(2020, 1, 1),
            date_to=date(2020, 1, 10),
            week_days=[1, 2, 3],
        ),
    ),
    (
        dict(
            time_from=time(8, 00, 00),
            time_to=time(17, 00, 00),
            date_from=date(2020, 1, 1),
            date_to=date(2020, 1, 10),
            week_days=[1, 2, 3],
        ),
        dict(
            time_from=time(10, 00, 00),
            time_to=time(13, 00, 00),
            date_from=date(2020, 1, 1),
            date_to=date(2020, 1, 10),
            week_days=[1, 2, 3],
        ),
    ),
    (
        dict(
            time_from=time(8, 00, 00),
            time_to=time(17, 00, 00),
            date_from=date(2020, 1, 1),
            date_to=date(2020, 1, 10),
            week_days=[1, 2, 3],
        ),
        dict(
            time_from=time(10, 00, 00),
            time_to=time(20, 00, 00),
            date_from=date(2020, 1, 1),
            date_to=date(2020, 1, 10),
            week_days=[1, 2, 3],
        ),
    ),
    (
        dict(
            time_from=time(22, 00, 00),
            time_to=time(11, 00, 00),
            date_from=date(2020, 1, 1),
            date_to=date(2020, 1, 10),
            week_days=[3, 4, 5],
        ),
        dict(
            time_from=time(10, 00, 00),
            time_to=time(20, 00, 00),
            date_from=date(2020, 1, 11),
            date_to=date(2020, 1, 20),
            week_days=[6, 7, 1],
        ),
    ),
]

tests_not = [
    (
        dict(
            time_from=time(8, 00, 00),
            time_to=time(17, 00, 00),
            date_from=date(2020, 1, 1),
            date_to=date(2020, 1, 10),
            week_days=[1, 2, 3],
        ),
        dict(
            time_from=time(17, 00, 00),
            time_to=time(4, 00, 00),
            date_from=date(2020, 1, 1),
            date_to=date(2020, 1, 10),
            week_days=[1, 2, 3],
        ),
    ),
    (
        dict(
            time_from=time(22, 00, 00),
            time_to=time(5, 00, 00),
            date_from=date(2020, 9, 1),
            date_to=date(2020, 9, 30),
            week_days=[2, 4],
        ),
        dict(
            time_from=time(8, 00, 00),
            time_to=time(17, 00, 00),
            date_from=date(2020, 9, 1),
            date_to=date(2020, 9, 30),
            week_days=[1, 3],
        ),
    ),
]
print('test ok:')
for i in tests_ok:
    men1 = Shift()
    men1.time_from = i[0]['time_from']
    men1.time_to = i[0]['time_to']
    men1.date_from = i[0]['date_from']
    men1.date_to = i[0]['date_to']
    men1.week_days = i[0]['week_days']

    men2 = Shift()
    men2.time_from = i[1]['time_from']
    men2.time_to = i[1]['time_to']
    men2.date_from = i[1]['date_from']
    men2.date_to = i[1]['date_to']
    men2.week_days = i[1]['week_days']

    print(Shift.compare(men1, men2))

print('test not ok:')
for i in tests_not:
    men1 = Shift()
    men1.time_from = i[0]['time_from']
    men1.time_to = i[0]['time_to']
    men1.date_from = i[0]['date_from']
    men1.date_to = i[0]['date_to']
    men1.week_days = i[0]['week_days']

    men2 = Shift()
    men2.time_from = i[1]['time_from']
    men2.time_to = i[1]['time_to']
    men2.date_from = i[1]['date_from']
    men2.date_to = i[1]['date_to']
    men2.week_days = i[1]['week_days']

    print(Shift.compare(men1, men2))
