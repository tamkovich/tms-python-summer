"""
Написать программу таймер. Программа при запуске принимает имя,
фамилию, часы, минуты и секунды. После программа начинает обратный
отсчет выводя оставшееся время. Программа должна хранить файл
логирования с информацией о том кто запускал программу и когда.
Пример:
00:00:03
00:00:02
00:00:01
ALARM!!!
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
hour = input('input hour: ')
minute = input('input minute: ')
second = input('input second: ')
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
        minute = 0
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
    break

log_file.write(f"{environ['USERNAME']} - "
               f"{lastname, firstname} - "
               f"{date.strftime('%d.%m.%Y')} "
               f"{date.strftime('%H:%M:%S')}\n")
log_file.close()


def timer(hours: int = 0, minutes: int = 0, seconds: int = 1) -> str:
    timer = timedelta(hours=abs(hours), minutes=abs(minutes), seconds=abs(seconds))

    while timer.seconds > 0:
        system('cls||clear')
        timer -= timedelta(seconds=1)
        sleep(1)
        print(f'{str(timer).split(".")[0]}')
    print('ALARM!!!')
    return f'ALARM!!!'


timer(hour, minute, second)
