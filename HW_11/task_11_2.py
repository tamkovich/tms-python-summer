class Car:
    def __init__(self, marca, model, year, speed):
        self.__marca = marca
        self.__model = model
        self.__year = year
        self.__speed = speed

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed):
        self.__speed = speed

    def speed_up(self, plus_speed=5):
        self.__speed += plus_speed

    def speed_down(self, plus_speed=5):
        self.__speed -= plus_speed

    def stop(self):
        self.__speed = 0

    def revers(self):
        self.__speed *= (-1)


audi = Car('Audi', 'A6', 2008, 120)

audi.speed_up(10)
audi.speed_down(30)
audi.revers()
# audi.stop()

print(audi.speed)
