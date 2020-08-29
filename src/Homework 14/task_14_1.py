# task_14_1
"""
Написать программу таймер. Программа при запуске принимает имя,
фамилию, часы, минуты и секунды. После программа начинает обратный
отсчет выводя оставшееся время. Программа должна хранить файл
логирования с информацией о том кто запускал программу и когда.
"""

import argparse
import datetime
import time

print(datetime.datetime.now())

parser = argparse.ArgumentParser()
parser.add_argument('-fn', '--first-name', required=True)
parser.add_argument('-ln', '--last-name', required=True)
parser.add_argument('echo')
args = parser.parse_args()

print('First name:', args.first_name)
print('Last name:', args.last_name)
print('Time:', args.echo)

time_list = args.echo.split(":")

for i in range(len(time_list)):
    try:
        time_list[i] = int(time_list[i])
    except ValueError:
        print("time must be int")

h = time_list[0]
m = time_list[1]
s = time_list[2]

time_in_seconds = h * 3600 + m * 60 + s

while time_in_seconds != 0:
    print(datetime.time(hour=h, minute=m, second=s))
    time_in_seconds -= 1

    if s != 0:
        s -= 1
    elif m != 0:
        m -= 1
        s += 59
    else:
        h -= 1
        m += 59
        s += 59

    time.sleep(1)

print("ALARM!!!")
