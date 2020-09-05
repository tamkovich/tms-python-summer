# task_14_2
"""
Создать программу Pomodoro.
На вход программа получает имя, фамилию, время для
фокусировки(по-умолчанию 25 минут), длину перерыва(по-умолчанию 5 минут),
количество циклов(по-умолчанию 4) и название задачи. Программа указывает
оставшееся время фокусировки, после сигнализирует о наступлении перерыва,
после сигнализирует о начале нового цикла фокусировки. Программа должна
вести файл лога о всех запусках.
"""
import time
import datetime
import typing


class MyTime:
    """
    Allows to work with time
    """

    def __init__(self, hours: int, minutes: int, seconds: int) -> None:
        """
        Constructor with attributes for time
        :param hours: hours
        :param minutes: minutes
        :param seconds: seconds
        """
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds


class Pomodoro:
    """
    Class allows to work with program Pomodoro
    """

    def __init__(
        self,
        fn: str,
        ln: str,
        name: str,
        time_work: MyTime,
        time_break: MyTime,
        time_pause: MyTime,
        cycles_number: int,
        numbers: int,
    ) -> None:
        """
        Constructor with some attributes for class
        :param fn: firstname
        :param ln: lastname
        :param name: task name
        :param time_work: time to task
        :param time_break: time for a break
        :param time_pause: time to focus
        :param cycles_number: number of cycles
        :param numbers: number of work cycles
        """
        self.fn = fn
        self.ln = ln
        self.name = name
        self.time_work = time_work
        self.time_break = time_break
        self.time_pause = time_pause
        self.cycles_number = cycles_number
        self.numbers = numbers

    def countdown(self) -> None:
        """
        Countdown for pomodoro
        :return: none
        """
        count, tmp = 0, 0

        while count != self.numbers:

            hours_work = self.time_work.hours
            minutes_work = self.time_work.minutes
            seconds_work = self.time_work.seconds
            work_time = all_time(hours_work, minutes_work, seconds_work)

            hours_break = self.time_break.hours
            minutes_break = self.time_break.minutes
            seconds_break = self.time_break.seconds
            break_time = all_time(hours_break, minutes_break, seconds_break)

            hours_pause = self.time_pause.hours
            minutes_pause = self.time_pause.minutes
            seconds_pause = self.time_pause.seconds
            pause_time = all_time(hours_pause, minutes_pause, seconds_pause)

            print("You can work")

            while work_time != 0:
                print(
                    datetime.time(
                        hour=hours_work, minute=minutes_work, second=seconds_work
                    )
                )
                work_time -= 1
                hours_work, minutes_work, seconds_work = timer(
                    hours_work, minutes_work, seconds_work
                )
                time.sleep(1)
            tmp += 1

            if count == self.numbers:
                print("Ended")
                break

            if tmp != self.cycles_number:
                print("PAUSE!")

                while break_time != 0:
                    print(
                        datetime.time(
                            hour=hours_break, minute=minutes_break, second=seconds_break
                        )
                    )
                    break_time -= 1
                    hours_break, minutes_break, seconds_break = timer(
                        hours_pause, minutes_break, seconds_break
                    )
                    time.sleep(1)

            if tmp == self.cycles_number:
                print("BIG PAUSE!")

                while pause_time != 0:
                    print(
                        datetime.time(
                            hour=hours_pause, minute=minutes_pause, second=seconds_pause
                        )
                    )
                    pause_time -= 1
                    hours_pause, minutes_pause, seconds_pause = timer(
                        hours_pause, minutes_pause, seconds_pause
                    )
                    time.sleep(1)
                    tmp = 0
                count += 1


def timer(h: int, m: int, s: int) -> typing.Tuple:
    """
    Timer for rime
    :param h: hours
    :param m: minutes
    :param s: seconds
    :return: new time
    """
    if s != 0:
        s -= 1
    elif m != 0:
        m -= 1
        s += 59
    else:
        h -= 1
        m += 59
        s += 59

    return h, m, s


def all_time(h: int, m: int, s: int) -> int:
    """
    Converting time into seconds
    :param h: hours
    :param m: minutes
    :param s: seconds
    :return: time in seconds
    """
    return h * 3600 + m * 60 + s


if __name__ == "__main__":
    firstname = input("Enter firstname: ")
    lastname = input("Enter firstname: ")
    name_work = input("Enter name work: ")
    number_of_cycles = input("Enter numbers of cycles: ")
    number = input("Enter numbers of work cycles: ")

    try:
        number_of_cycles = int(number_of_cycles)
        number = int(number)
    except ValueError:
        print("Must be int")

    work_time = MyTime(0, 25, 0)
    break_time = MyTime(0, 3, 0)
    pause_time = MyTime(0, 15, 0)
    pomodoro = Pomodoro(
        firstname,
        lastname,
        name_work,
        work_time,
        break_time,
        pause_time,
        number_of_cycles,
        number,
    )

    pomodoro.countdown()

    with open("task_14_2.txt", "a") as file:
        file.writelines(f"{firstname} {lastname} - {name_work}\n")
