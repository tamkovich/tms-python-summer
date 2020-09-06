"""
 Написать программу таймер.
 Программа при запуске принимает имя, фамилию, часы, минуты и секунды.
 После программа начинает обратный отсчет выводя оставшееся время.
 Программа должна хранить файл логирования с информацией о том
 кто запускал программу и когда.
"""


import time
import sys
import argparse
print(sys.argv)


parser = argparse.ArgumentParser()
parser.add_argument('-fn', '--first-name', required=True)
parser.add_argument('-ln', '--last-name', required=True)
parser.add_argument('-hou', '--my_hours', required=True)
parser.add_argument('-min', '--my_minutes', required=True)
parser.add_argument('-sec', '--my_seconds', required=True)
args = parser.parse_args()
print(args)
print('First name:', args.first_name)
print('Last name:', args.last_name)
print(args.my_hours, ':', args.my_minutes, ':', args.my_seconds)
args.my_hours = int(args.my_hours) * 3600
args.my_minutes = int(args.my_minutes) * 60
args.my_seconds = int(args.my_seconds)
time.sleep(args.my_seconds)
time.sleep(args.my_minutes)
time.sleep(args.my_hours)
print('ALARM!')


with open('new_file.txt', 'w') as f:
    f.write(f'First name:, {args.first_name}',
            f'Last name:, {args.last_name}',
            f'{args.my_hours} : {args.my_minutes} : {args.my_seconds}')
f.close()
