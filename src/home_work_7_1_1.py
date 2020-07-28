
namber = int(input('Выберите тип перевода единиц и введите соответствующее число для выбора единиц перевода:'))
while namber == 0:
  print('oшибка')
  break
else:
 choice = int(input('Выберите число:'))
if namber == 1:
    print('сантиметр', choice * 2.54)
elif namber == 2:
    print('дюйм', (choice / 2.54))
elif namber == 3:
    print('километр', choice * 1.609)
elif namber == 4:
    print('миля', choice / 1.609)
elif namber == 5:
    print('килограмм', choice / 2.205)
elif namber == 6:
    print('фунт', choice * 2 / 205)
elif namber == 7:
    print('грамм', choice * 28.35)
elif namber == 8:
    print('унция', choice / 28.35)
elif namber == 9:
    print('литр', choice * 4.546)
elif namber == 10:
    print('галлон', choice / 4.546)
elif namber == 11:
    print('литр', choice * 2.113)
elif namber == 12:
    print('пинта', choice / 2.113)

