import unittest
from datetime import date, time
from test import Shift


class ShiftTestCase(unittest.TestCase):
    """
    class for testing class 'Shift'
    return: True for crosses shifts. False - not crosses shifts.
    """

    def test_shift_True(self):
        t1 = Shift(**tests_true[0][0])
        t2 = Shift(**tests_true[0][1])
        compare1 = Shift.__cmp__(t1, t2)

        t1 = Shift(**tests_true[1][0])
        t2 = Shift(**tests_true[1][1])
        compare2 = Shift.__cmp__(t1, t2)

        t1 = Shift(**tests_true[2][0])
        t2 = Shift(**tests_true[2][1])
        compare3 = Shift.__cmp__(t1, t2)

        t1 = Shift(**tests_true[3][0])
        t2 = Shift(**tests_true[3][1])
        compare4 = Shift.__cmp__(t1, t2)

        t1 = Shift(**tests_true[4][0])
        t2 = Shift(**tests_true[4][1])
        compare5 = Shift.__cmp__(t1, t2)

        t1 = Shift(**tests_true[5][0])
        t2 = Shift(**tests_true[5][1])
        compare6 = Shift.__cmp__(t1, t2)

        self.assertEqual((compare1, compare2, compare3,
                          compare4, compare5, compare6),
                         (True, True, True, True, True, True))

    def test_shift_False(self):
        t1 = Shift(**tests_false[0][0])
        t2 = Shift(**tests_false[0][1])
        compare1 = Shift.__cmp__(t1, t2)

        t1 = Shift(**tests_false[1][0])
        t2 = Shift(**tests_false[1][1])
        compare2 = Shift.__cmp__(t1, t2)

        self.assertEqual((compare1, compare2),
                         (False, False))


tests_true = [
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

tests_false = [
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

if __name__ == "main":
    unittest.main()
