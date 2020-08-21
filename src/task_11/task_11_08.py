"""
Сделать все атрибуты класса Dog приватными.
Сделать для каждого атрибута getter и setter используя декораторы.
Все change методы удалить
"""

class Dog:
    """создан класс Собака"""
    def __init__(self, name, age, color, breed, weight):
        self.__name = name
        self.__age = age
        self.__color = color
        self.__breed = breed
        self.__weight = weight

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def color(self):
        return self.__color

    @property
    def breed(self):
        return self.__breed

    @property
    def weight(self):
        return self.__weight

    @color.setter
    def color(self, color):
        self.__color = color

    @breed.setter
    def breed(self, breed):
        self.__breed = breed

    @weight.setter
    def weight(self, weight):
        self.__weight = weight


dog1 = Dog("Ali", 12, 'black', "dog", 14)
print(dog1.name, dog1.color, dog1.weight, dog1.age, dog1.breed, sep="\n")
