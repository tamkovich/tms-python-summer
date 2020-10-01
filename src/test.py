from datetime import date, time

class Shift:
    def __init__(self, time_from: time,
                 time_to: time,
                 date_from: date,
                 date_to: date,
                 week_days: list):
        """
        class 'work shift'
        :param time_from: time of start work shift
        :param time_to: time of end work shift
        :param date_from: date of start work shift
        :param date_to: date of end work shift
        :param week_days: days in work week
        """

        self.time_from = time_from
        self.time_to = time_to
        self.date_from = date_from
        self.date_to = date_to
        self.week_days = week_days

    def __str__(self):
        return f'{self.time_from}, ' \
               f'{self.time_to}, ' \
               f'{self.date_from}, ' \
               f'{self.date_to}, ' \
               f'{self.week_days}'

    def __cmp__(self, other):
        if (self.date_to < other.date_from and
            self.week_days[-1] != (other.week_days[0]-1)) or \
                (other.date_to < self.date_from and
                 other.week_days[-1] != (self.week_days[0]-1)):
            return False
        else:
            if (set(self.week_days) & set(other.week_days)) == set() and \
                    (self.time_from < self.time_to and other.time_from < other.time_to):
                return False
            else:
                if (self.time_from < self.time_to <= other.time_from < other.time_to or
                        other.time_from < other.time_to <= self.time_from < self.time_to or
                        other.time_to <= self.time_from < other.time_from <= self.time_to or
                        self.time_to <= other.time_from < self.time_from <= other.time_to or
                        other.time_from >= self.time_to < other.time_to < self.time_from or
                        self.time_from >= other.time_to < self.time_to < other.time_from):
                    return False
                else:
                    return True
