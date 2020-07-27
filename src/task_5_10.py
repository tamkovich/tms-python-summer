"""
Создать список поездов. Структура словаря: номер поезда,
пункт и время прибытия, пункт и время отбытия. Вывести все сведения о поездах,
время пребывания в пути которых превышает 7 часов 20 минут.
"""

from datetime import timedelta
spisok_poezdov = [
    {
        "number": "A",
        "point_out": "Minsk",
        "out_time": timedelta(hours=12, minutes=45),
        "point_in": "Brest",
        "time_in": timedelta(hours=22, minutes=00)
     },
    {
        "number": "B",
        "point_out": "Minsk",
        "out_time": timedelta(hours=00, minutes=45),
        "point_in": "Vitebsk",
        "time_in": timedelta(hours=15, minutes=30)
     },
    {
        "number": "C",
        "point_out": "Minsk",
        "out_time": timedelta(hours=9, minutes=10),
        "point_in": "Grodno",
        "time_in": timedelta(hours=21, minutes=00)
     },
    {
        "number": "D",
        "point_out": "Minsk",
        "out_time": timedelta(hours=15, minutes=30),
        "point_in": "Gomel",
        "time_in": timedelta(hours=23, minutes=40)
    },
    {
        "number": "E",
        "point_out": "Minsk",
        "out_time": timedelta(hours=12, minutes=30),
        "point_in": "Borisov",
        "time_in": timedelta(hours=16, minutes=40)
    },
    {
        "number": "F",
        "point_out": "Minsk",
        "out_time": timedelta(hours=11, minutes=10),
        "point_in": "Baranovichi",
        "time_in": timedelta(hours=13, minutes=40)
    }
]

for i in spisok_poezdov:
    delta = i["time_in"] - i["out_time"]

    if delta >= timedelta(hours=7, minutes=20):
        print(
            f'поезд номер {i["number"]} из {i["point_out"]} в {i["point_in"]} | '
            f'время отправления: {i["out_time"]}, время прибытия: {i["time_in"]}.'
        )
