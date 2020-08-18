# task_11_2
"""Создать класс Car. Атрибуты: марка, модель, год выпуска, скорость(по
умолчанию 0). Методы: увеличить скорости(скорость + 5), уменьшение
скорости(скорость - 5), стоп(сброс скорости на 0), отображение скорости,
разворот(изменение знака скорости). Все атрибуты приватные."""


class Car:
    """
    Class describes the attributes and methods of cars
    """
    def __init__(self, brand: str, model: str, year: int, velocity=0):
        """
        Constructor of class Car
        :param brand: car brand
        :param model: model of brand
        :param year: year is issue
        :param velocity: car speed
        """
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__velocity = velocity

    def increase_velocity(self):
        """
        Increase velocity
        :return: new velocity
        """
        return self.__velocity + 5

    def decrease_velocity(self):
        """
        Decrease velocity
        :return: new velocity
        """
        return self.__velocity - 5

    def stop(self):
        """
        The car stops
        :return: velocity = 0
        """
        return 0

    def reversal(self):
        """
        The car is turning
        :return: velocity with " - "
        """
        return -1 * self.__velocity

    @property
    def velocity(self):
        return self.__velocity

    @velocity.setter
    def velocity(self, velocity):
        self.__velocity = velocity


car = Car("Audi", "A6", 2017, 30)
print(car.__dict__)

car.velocity = car.increase_velocity()
print(car.__dict__)

car.velocity = car.decrease_velocity()
print(car.__dict__)

car.velocity = car.stop()
print(car.__dict__)

car.velocity = 60

car.velocity = car.reversal()
print(car.__dict__)
