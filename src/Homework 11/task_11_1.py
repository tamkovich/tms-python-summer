# task_11_1
"""Создать пять классов описывающие реальные объекты. Каждый класс
должен содержать минимум три приватных атрибута, конструктор, геттеры
и сеттеры для каждого атрибута, два метода."""


class Dog:
    """
    Class describes the attributes and methods of dogs
    """
    def __init__(self, name: str, age: int, breed: str):
        """
        Constructor of class Dog
        :param name: dog's name
        :param age: dog age
        :param breed: dog breed
        """
        self.__name = name
        self.__age = age
        self.__breed = breed

    def jump(self):
        """
        The dog will start jumping
        :return: nothing
        """
        print("Jump!")

    def sound(self):
        """
        The dog will bark
        :return: nothing
        """
        print("Woof!")

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
    def breed(self):
        return self.__breed

    @breed.setter
    def breed(self, breed):
        self.__breed = breed


class Cat:
    """
    Class describes the attributes and methods of cats
    """
    def __init__(self, name: str, age: int, breed: str):
        """
        Constructor of class Cat
        :param name: cat's name
        :param age: cat age
        :param breed: cat breed
        """
        self.__name = name
        self.__age = age
        self.__breed = breed

    def jump(self):
        """
        The cat will start jump
        :return: nothing
        """
        print("Jump!")

    def sound(self):
        """
        The dog will meow
        :return: nothing
        """
        print("Meow!")

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
    def breed(self):
        return self.__breed

    @breed.setter
    def breed(self, breed):
        self.__breed = breed


class Car:
    """
    Class describes the attributes and methods of cars
    """
    def __init__(self, number: str, year: int, brand: str):
        """
        Constructor of class Car
        :param number: car's number
        :param year: year of issue
        :param brand: car brand
        """
        self.__number = number
        self.__year = year
        self.__brand = brand

    def break_car(self):
        """
        Car is breaking
        :return: nothing
        """
        print("Break!")

    def sound(self):
        """
        The car will make a sound
        :return: nothing
        """
        print("Beeb!")

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        self.__number = number

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        self.__year = year

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, brand):
        self.__brand = brand


class Food:
    """
    Class describes the attributes and methods of food
    """
    def __init__(self, name: str, quantity: int, price: float):
        """
        Constructor of class Food
        :param name: food name
        :param quantity: amount of food
        :param price: price
        """
        self.__name = name
        self.__quantity = quantity
        self.__price = price

    def spoiled(self):
        """
        Food spoiled
        :return: nothing
        """
        print("Spoiled!")

    def ended(self):
        """
        Food ended
        :return: nothing
        """
        print("Ended!")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity):
        self.__quantity = quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price


class Fruit(Food):
    """
    Child class, useful method is added
    """
    def useful(self):
        """
        Fruits is very useful
        :return: nothing
        """
        print("Fruits are very healthy. Eat them")


dog = Dog("Sam", 4, "shepherd")
print(dog.__dict__)
dog.name, dog.age, dog.breed = "Tim", 7, "shepherd"
print(dog.__dict__)
f"{dog.sound()}\n{dog.jump()}\n"

cat = Cat("Tom", 2, "siamese")
print(cat.__dict__)
cat.name, cat.age, cat.breed = "Tom", 3, "siamese"
print(cat.__dict__)
f"{cat.sound()}\n{cat.jump()}\n"

car = Car("0456AK-7", 2017, "Ford")
print(car.__dict__)
car.number, car.year, car.brand = "9999EC-7", 2017, "Ford"
print(car.__dict__)
f"{car.sound()}\n{car.break_car()}\n"

food = Food("bread", 100, 2.30)
print(food.__dict__)
food.name, food.quantity, food.price = "bread", 56, 2.45
print(food.__dict__)
f"{food.spoiled()}\n{food.ended()}\n"

fruit = Fruit("apple", 200, 1.56)
print(fruit.__dict__)
fruit.name, fruit.quantity, fruit.price = "bread", 56, 2.45
print(fruit.__dict__)
f"{fruit.useful()}\n{food.spoiled()}\n"
