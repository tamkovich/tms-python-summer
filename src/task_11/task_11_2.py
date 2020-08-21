"""
Создать класс Car. Атрибуты: марка, модель, год выпуска, скорость(по
умолчанию 0). Методы: увеличить скорости(скорость + 5), уменьшение
скорости(скорость - 5), стоп(сброс скорости на 0), отображение скорости,
разворот(изменение знака скорости). Все атрибуты приватные.
"""

class Car:
    """Created class Car"""
    def __init__(self, mark: str, model: str, year: str, max_speed: int, speed: int = 0):
        self.__mark = mark
        self.__model = model
        self.__year = year
        self.__max_speed = max_speed
        self.__speed = speed

    @property
    def mark(self):
        return self.__mark

    @mark.setter
    def mark(self, mark):
        self.__mark = mark

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        self.__model = model

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        self.__year = year

    @property
    def max_speed(self):
        return self.__max_speed

    @max_speed.setter
    def max_speed(self, max_speed):
        self.__max_speed = max_speed

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed):
        self.__speed = speed

    def increase_speed(self):
        self.speed += 5
        if self.speed > self.speed - 5:
            self.speed = self.speed

    def reduce_speed(self):
        self.speed -= 5
        if self.speed < 5:
            self.speed = 0

    def stop(self):
        self.speed = 0
        print(f'car stopped')

    def display_speed(self):
        print(f"speed now: {self.speed} km/h")

    def reversal(self):
        self.speed = -self.speed
        print(f'car is going in another side now')


car1 = Car('Audi', "TT", "2010", 250, 110)
car1.increase_speed()
car1.increase_speed()
car1.display_speed()
car1.reversal()
print(car1.__dict__)
car1.stop()