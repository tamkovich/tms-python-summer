'''
Задание 10.5
'''
a=[]
with open('task_10_4.txt', 'r') as f1, open('task_10_4.txt', 'w') as f2:
    lines = f1.readlines()
for line in lines:
    if line == '0':
        a.append('1')
    elif line == '1':
        a.append('0')
    else:
        a.append(line)
f2.write(''.join(a))
f1.close()
f2.close()
