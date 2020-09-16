from datetime import time, date
from unittest import TestCase

from test import Shift


class CrossingTest(TestCase):
    def test_ok(self):
        men1 = Shift(**tests_ok[0][0])
        men2 = Shift(**tests_ok[0][1])
        crossing1 = Shift.compare(men1, men2)

        men3 = Shift(**tests_ok[1][0])
        men4 = Shift(**tests_ok[1][1])
        crossing2 = Shift.compare(men3, men4)

        men5 = Shift(**tests_ok[2][0])
        men6 = Shift(**tests_ok[2][1])
        crossing3 = Shift.compare(men5, men6)

        men7 = Shift(**tests_ok[3][0])
        men8 = Shift(**tests_ok[3][1])
        crossing4 = Shift.compare(men7, men8)

        men9 = Shift(**tests_ok[3][0])
        men10 = Shift(**tests_ok[3][1])
        crossing5 = Shift.compare(men9, men10)

        men11 = Shift(**tests_ok[3][0])
        men12 = Shift(**tests_ok[3][1])
        crossing6 = Shift.compare(men11, men12)

        self.assertEqual([crossing1, crossing2, crossing3, crossing4, crossing5, crossing6],
                         [True, True, True, True, True, True])

    def test_not(self):
        men1 = Shift(**tests_not[0][0])
        men2 = Shift(**tests_not[0][1])
        crossing1 = Shift.compare(men1, men2)

        men3 = Shift(**tests_not[1][0])
        men4 = Shift(**tests_not[1][1])
        crossing2 = Shift.compare(men3, men4)

        self.assertEqual([crossing1, crossing2], [False, False])


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
