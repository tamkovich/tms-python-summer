file_ish = open('10_5_1.txt','r')
file_chet = open('10_5_2.txt','a')
file_nechet = open('10_5_3.txt','a')

for i in range(10):
    if i % 2 == 0:
        file_chet.write(file_ish.readline())
    else:
        file_nechet.write(file_ish.readline())

file_chet.close
file_nechet.close
file_ish.close
