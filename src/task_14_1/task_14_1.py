"""
Написать программу таймер. Программа при запуске принимает имя,
фамилию, часы, минуты и секунды. После программа начинает обратный
отсчет выводя оставшееся время. Программа должна хранить файл
логирования с информацией о том кто запускал программу и когда.
"""


import classes
import argparse
import datetime

parser = argparse.ArgumentParser()
parser.add_argument('-fn', '--first-name', required=True)
parser.add_argument('-ln', '--last-name', required=True)
parser.add_argument('time')
args = parser.parse_args()

print('First name:', args.first_name)
print('Last name:', args.last_name)
print('time:', args.time)
addtime = args.time

time1 = classes.Timer(addtime)
print(time1.countdown_time())

with open('logs.txt', 'a') as f:
    f.write(f'{args.first_name} {args.last_name}, '
            f'{datetime.datetime.now()} \n')