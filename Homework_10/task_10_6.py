file_one = open('task_10_6_1.txt')
file_two = open('task_10_6_2.txt')
i = 1
while True:
    line_1 = file_one.readline()
    line_2 = file_two.readline()
    if not line_1 or not line_2:
        print('все строки одинаковые')
        break
    if line_1 == line_2:
        i += 1
        continue
    elif line_1 != line_2:
        print(f'в {i} строке найдены различия')
        break
