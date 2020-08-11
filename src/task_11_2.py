"""
Создать класс Car. Атрибуты: марка, модель, год  выпуска, скорость(по умолчанию 0).
Методы: увеличить скорости(скорость + 5), уменьшение скорости(скорость  - 5),
стоп(сброс скорости на 0), отображение скорости, разворот(изменение знака скорости).
Все атрибуты приватные.
"""



class Car:
    def __init__(self, mark, model, year, speed):
        self.__mark = mark
        self.__model = model
        self.__year = year
        self.__speed = speed
    def increase(self):
        self.__speed += 5
    def decrease(self):
        self.__speed -= 5
    def set_zero(self):
        self.__speed = 0
    def show(self):
         print(self.__speed)
    def minus(self):
        self.__speed *= (-1)

tayota = Car('x4', 'new', '2021', 0)
tayota.show()
