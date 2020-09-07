"""
Создать программу Pomodoro.
На вход программа получает имя, фамилию, время для
фокусировки(по-умолчанию 25 минут), длину перерыва(по-умолчанию 5 минут),
количество циклов(по-умолчанию 4) и название задачи. Программа указывает
оставшееся время фокусировки, после сигнализирует о наступлении перерыва,
после сигнализирует о начале нового цикла фокусировки. Программа должна
вести файл лога о всех запусках.
"""


import classes
import argparse
import datetime


parser = argparse.ArgumentParser(description='Pomodoro')
parser.add_argument('-fn', '--first-name', required=True)
parser.add_argument('-ln', '--last-name', required=True)
parser.add_argument('name_of_task', type=str)
parser.add_argument('time_focus', nargs='?', type=int or float, default=25)
parser.add_argument('time_pause', nargs='?', type=int or float, default=5)
parser.add_argument('numb_of_cycles', nargs='?', type=int, default=4)
args = parser.parse_args()

print('First name:', args.first_name)
print('Last name:', args.last_name)
print('name_of_task:', args.name_of_task)
print('time_focus:', args.time_focus)
print('time_pause:', args.time_pause)
print('numb_of_cycles:', args.numb_of_cycles)


pom1 = classes.Pomodoro(args.time_focus, args.time_pause)
for i in range(args.numb_of_cycles):
    print(pom1.focus())
    print(pom1.pause())
print('End Pomodoro!')

with open('Pomodoro_logs.txt', 'a') as f:
    f.write(f'{args.first_name} {args.last_name}, '
            f'task: {args.name_of_task}, '
            f'{datetime.datetime.now()} \n')
