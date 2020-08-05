my_file_open = open('task_10_4_(1).txt', 'r')
my_file_copy = open('task_10_4_(2).txt', 'w')
for line in my_file_open.readlines():
    pust = []
    for i in line:
        if i == '0':
            pust.append('1')
        elif i == '1':
            pust.append('0')
        else:
            pust.append(i)
    my_file_copy.write(''.join(pust))
my_file_open.close()
my_file_copy.close()
