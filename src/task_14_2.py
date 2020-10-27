"""На вход программа получает имя,
фамилию, время для фокусировки(по-умолчанию 25 минут),
длину перерыва(по-умолчанию 5 минут),
количество циклов(по-умолчанию 4) и название задачи.
Программа указывает оставшееся время фокусировки, после
сигнализирует о наступлении перерыва, после сигнализирует
о начале нового цикла фокусировки. Программа
должна вести файл лога о всех запусках. """


from time import sleep
import sys
import argparse
print(sys.argv)


parser = argparse.ArgumentParser()
parser.add_argument('-fn', '--first-name', required=True)
parser.add_argument('-ln', '--last-name', required=True)
parser.add_argument('-min', '--focus_time', required=True)
parser.add_argument('-min2', '--break_time', required=True)
args = parser.parse_args()
args.focus_time = int(args.focus_time) * 60
args.break_time = int(args.break_time) * 60
exit_condition = 0
while exit_condition < 4:
    tmp1 = args.focus_time
    tmp2 = args.break_time
    sleep(tmp1)
    sleep(tmp2)
    exit_condition += 1
with open('tessst.txt', 'w') as f:
    f.write(Namespace)
f.close()
# в файл почему-то не записывает
