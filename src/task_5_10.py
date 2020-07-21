import datetime
raspis = [
    {
        'train number': '18',
        'point of arrival': 'Minsk',
        'time of arrival': datetime.timedelta(hours=7, minutes=40),
        'departur point': 'Brest',
        'departure time': datetime.timedelta(hours=4, minutes=30)
    },
    {
        'train number': '43',
        'point of arrival': 'Grodno',
        'time of arrival': datetime.timedelta(hours=23, minutes=40),
        'departur point': 'Moskow',
        'departure time': datetime.timedelta(hours=11, minutes=00)
    }
]
for i in raspis:
    time_travel = i['time of arrival'] - i['departure time']
    if time_travel > datetime.timedelta(hours=7, minutes=20):
        print(f"train number: {i['train number']}")
        print(f"point of arrival: {i['point of arrival']}")
        print(f"time of arrival: {i['time of arrival']}")
        print(f"departur point: {i['departur point']}")
        print(f"departure time: {i['departure time']}")
