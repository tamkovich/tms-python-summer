"""Создать класс Car. Атрибуты: марка, модель, год выпуска, скорость(по
умолчанию 0). Методы: увеличить скорости(скорость + 5), уменьшение
скорости(скорость - 5), стоп(сброс скорости на 0), отображение скорости,
разворот(изменение знака скорости). Все атрибуты приватные."""

class Car:
    def __init__(self, car_brend, model, year, speed=0):
        self.__car_brend = car_brend
        self.__model = model
        self.__year = year
        self.__speed = speed

    def increase_speed(self, speed=5):
        self.__speed += speed

    def reduce_speed(self, speed=5):
        self.__speed -= speed

    def stop(self):
        self.__speed = 0

    def show_speed(self):
        print(self.__speed)

    def turn_around(self):
        self.__speed *= -1


car = Car('BMW', 'M3', 2000)
car.show_speed()
car.increase_speed()
car.show_speed()
car.reduce_speed(12)
car.show_speed()
car.turn_around()
car.show_speed()
car.stop()
car.show_speed()

