"""
Создать класс Car. Атрибуты: марка, модель, год выпуска, скорость(по
умолчанию 0). Методы: увеличить скорости(скорость + 5), уменьшение
скорости(скорость - 5), стоп(сброс скорости на 0), отображение скорости,
разворот(изменение знака скорости). Все атрибуты приватные.
"""

class Car:
    def __init__(self, brand, model, year_of_issue, speed=0):
        self.__brand = brand
        self.__model = model
        self.__year_of_issue = year_of_issue
        self.__speed = speed

    @property
    def speed(self):
        return self.__speed

    def speed_upper(self):
        self.__speed += 5

    def speed_down(self):
        self.__speed -= 5

    def speed_stop(self):
        self.__speed = 0

    def reversal(self, sign):
        self.__speed *= -1
