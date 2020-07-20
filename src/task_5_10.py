# Создать список поездов. Структура словаря: номер поезда,
# пункт и время прибытия, пункт и время отбытия. Вывести все сведения о поездах,
# время пребывания в пути которых превышает 7 часов 20 минут.[02-7.3-ML02]
d = [
    {"number": "20", "point_A": "Minsk", "start": "04:00", "point_B": "Mogilev", "end": "15:15"},
    {"number": "A30", "point_A": "Mogilev", "start": "13:30", "point_B": "Minsk", "end": "16:45"}
     ]
for dictionary in d:
    for key, value in dictionary.items():
        print(f"{key}: {value}", end='\t\t\t')
for d in d:
    tmp_A = d["start"].split(":")
    tmp_B = d["end"].split(":")
    time_A = datetime.timedelta(hours=int(tmp_A[0]), minutes=int(tmp_A[1]))
    time_B = datetime.timedelta(hours=int(tmp_B[0]), minutes=int(tmp_B[1]))

    if time_B - time_A > datetime.timedelta(hours=7, minutes=20):
        print(time_B - time_A)
        break