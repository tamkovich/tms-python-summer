# task_5_10
"""Создать список поездов. Структура словаря: номер поезда,
пункт и время прибытия, пункт и время отбытия. Вывести все сведения о поездах,
время пребывания в пути которых превышает 7 часов 20 минут"""

import datetime

list_of_trains = [
    {"number": "10", "point_A": "Minsk", "start": "10:30",
     "point_B": "Moscow", "end": "23:45"},
    {"number": "20", "point_A": "Minsk", "start": "04:00",
     "point_B": "Riga", "end": "15:15"},
    {"number": "A30", "point_A": "Soligorsk", "start": "13:30",
     "point_B": "Minsk", "end": "16:45"}
]

print("All trains:")
for dictionary in list_of_trains:
    for key, value in dictionary.items():
        print(f"{key}: {value}", end='\t\t\t')
    print()

print("\nAll trains whose travel time more than 7h and 20m: ")
for i in list_of_trains:
    for key, value in i.items():
        tmp_A = i["start"].split(":")
        tmp_B = i["end"].split(":")

        time_A = datetime.timedelta(hours=int(tmp_A[0]), minutes=int(tmp_A[1]))
        time_B = datetime.timedelta(hours=int(tmp_B[0]), minutes=int(tmp_B[1]))

        if time_B - time_A > datetime.timedelta(hours=7, minutes=20):
            print(f"{key}: {value}", end='\t\t\t')
    print()
