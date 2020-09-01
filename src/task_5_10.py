# Создать список поездов. Структура словаря: номер поезда,
# пункт и время прибытия, пункт и время отбытия. Вывести все сведения о поездах,
# время пребывания в пути которых превышает 7 часов 20 минут.

import datetime


class Space_and_time():
    time = datetime.time
    place = None

    def __init__(self, time: datetime.time, place: str):
        """
        fills 'time' and 'place' fields of 'Space_and_time' class
        :param time: time in 'hours : minutes : seconds' format
        :param place: place in 'string' format
        """
        self.time = time
        self.place = place


class TrainList():
    train_list = {}
    departure = {}
    destination = {}

    def add_train(self, train_num: int, in_departure: Space_and_time, in_destination: Space_and_time):
        """
        add train info to 'train_list'
        :param train_num: train number
        :param in_departure: departure place and time
        :param in_destination: destination place and time
        """
        self.train_list[train_num] = [{in_departure.place: in_departure.time},
                                      {in_destination.place: in_destination.time}]

    def show_train_list(self):
        """
        print train_list field
        """
        print(self.train_list)

    def get_travel_time(self, train_num: int):
        """
        returns time interval between departure and destination time of train with number 'train_num'
        :param train_num: number of train
        :return: time interval
        """
        train = self.train_list[train_num]
        train_departure, train_destination = train
        t0 = list(train_departure.values())
        t1 = list(train_destination.values())

        return datetime.datetime.strptime(str(t1.__getitem__(0)), '%H:%M:%S') - datetime.datetime.strptime(
            str(t0.__getitem__(0)), '%H:%M:%S')

    def list_len(self):
        """
        returns 'train_list' fields length
        """
        return len(self.train_list)

    def find_more_delta(self, delta: datetime.timedelta):
        """
        find time intervals between departure and destination time which more then 'delta'
        :param delta: time interval
        :return: train list with trains which have travel time more then 'delta'
        """
        result = {}
        for key in self.train_list.keys():
            if self.get_travel_time(key) > delta:
                result[key] = self.train_list[key]

        return result


train_list = TrainList()

space_time_a = Space_and_time(datetime.time(3, 5, 12), 'A')
space_time_b = Space_and_time(datetime.time(5, 12, 23), 'B')

space_time_a_1 = Space_and_time(datetime.time(3, 5, 12), 'A')
space_time_b_1 = Space_and_time(datetime.time(18, 12, 23), 'B')

train_list.add_train(5, space_time_a, space_time_b)
train_list.add_train(45, space_time_a_1, space_time_b_1)

train_list.show_train_list()

print(train_list.find_more_delta(datetime.timedelta(days=0, hours=7, minutes=40)))
