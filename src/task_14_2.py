"""
Создать программу Pomodoro.
На вход программа получает имя, фамилию, время для
фокусировки(по-умолчанию 25 минут), длину перерыва(по-умолчанию 5 минут),
количество циклов(по-умолчанию 4) и название задачи. Программа указывает
оставшееся время фокусировки, после сигнализирует о наступлении перерыва,
после сигнализирует о начале нового цикла фокусировки. Программа должна
вести файл лога о всех запусках.
"""

from os import makedirs, system, environ
from datetime import datetime, timedelta
from time import sleep

try:
    makedirs('logs')
except FileExistsError:
    pass
date = datetime.now()
log_date = f'logs/log_{date.strftime("%d-%m-%Y")}.txt'
try:
    log_file = open(log_date, 'a', encoding='utf8')
except FileNotFoundError:
    log_file = open(log_date, 'w', encoding='utf8')
firstname = input('input firstname: ')
lastname = input('input lastname: ')
task_name = input('input task name: ')
hour = input('input hour: ')
minute = input('input minute: ')
second = input('input second: ')
break_time = input('input break time: ')
cycle = input('input cycle: ')
while True:
    if hour == "":
        hour = 0
    else:
        if str(hour).isdigit():
            hour = int(hour)
        else:
            hour = input('re-enter hour: ')
            continue
    if minute == "":
        minute = 25
    else:
        if str(minute).isdigit():
            minute = int(minute)
        else:
            minute = input('re-enter minute: ')
            continue
    if second == "":
        second = 0
    else:
        if str(second).isdigit():
            second = int(second)
        else:
            second = input('re-enter second: ')
            continue
    if break_time == "":
        break_time = 5
    else:
        if str(break_time).isdigit():
            break_time = int(break_time)
        else:
            break_time = input('re-enter break time: ')
            continue
    if cycle == "":
        cycle = 5
    else:
        if str(cycle).isdigit():
            cycle = int(cycle)
        else:
            cycle = input('re-enter cycle: ')
            continue
    break

log_file.write(f"{environ['USERNAME']} - "
               f"{lastname, firstname} - "
               f"{task_name} - "
               f"{date.strftime('%d.%m.%Y')} "
               f"{date.strftime('%H:%M:%S')}\n")
log_file.close()


def timer(
        hours: int,
        minutes: int,
        seconds: int,
        break_times: int = 5,
        cycles: int = 4
):
    timer = timedelta(hours=abs(hours), minutes=abs(minutes), seconds=abs(seconds))

    while cycles > 0:
        print('Start focusing!!!')
        while timer.seconds > 0:
            system('cls||clear')
            timer -= timedelta(seconds=1)
            sleep(1)
            print(f'{str(timer).split(".")[0]}')
        print('Coffee Break!!!')
        sleep(break_times * 60)
        cycles -= 1
    print('ALARM!!!')


timer(hour, minute, second, break_time, cycle)
