"""
Создать пять классов описывающие реальные объекты.
Каждый класс должен содержать минимум три приватных атрибута,
конструктор, геттеры и сеттеры для каждого атрибута, два метода
"""

class Tv:
    def show(self):
        print("shows tv Shows")

    def sound(self):
        print("makes sounds")

    def __init__(self, quality, price, size):
        self.__quality = quality
        self.__price = price
        self.__size = size

    @property
    def x(self):
        return self.__quality

    @x.setter
    def quality(self, quality):
        self.__quality = quality

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        self.__size = size


class Languages:
    def speak(self):
        print("word")

    def read(self):
        print("text")

    def __init__(self, sounds, letters, phrase):
        self.__sounds = sounds
        self.__letters = letters
        self.__phrase = phrase

    @property
    def y(self):
        return self.__sounds

    @y.setter
    def sounds(self, sounds):
        self.__sounds = sounds

    @property
    def letters(self):
        return self.__letters

    @letters.setter
    def price(self, letters):
        self.__letters = letters

    @property
    def phrase(self):
        return self.__phrase

    @phrase.setter
    def phrase(self, phrase):
        self.__phrase = phrase


class Cars:
    def drive(self):
        print("*driving*")

    def drift(self):
        print("*drifting*")

    def __init__(self, colour, appereance, speed):
        self.__appereance = appereance
        self.__colour = colour
        self.__speed = speed

    @property
    def fun(self):
        return self.__colour

    @fun.setter
    def colour(self, colour):
        self.__colour = colour

    @property
    def look(self):
        return self.__appereance

    @look.setter
    def price(self, appereance):
        self.__appereance = appereance

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed):
        self.__speed = speed


class Human:
    def live(self):
        print("you r alive")

    def death(self):
        print("you r dead")

    def __init__(self, man, woman, kid):
        self.__man = man
        self.__woman = woman
        self.__kid = kid

    @property
    def man(self):
        return self.__man

    @man.setter
    def man(self, man):
        self.__man = man

    @property
    def woman(self):
        return self.__woman

    @woman.setter
    def woman(self, woman):
        self.__woman = woman

    @property
    def kid(self):
        return self.__kid

    @kid.setter
    def kid(self, kid):
        self.__kid = kid


class Plant:
    def grow(self):
        print("plant grows")

    def give(self):
        print("plant gives seeds")

    def __init__(self, tree, grass, bush):
        self.__tree = tree
        self.__grass = grass
        self.__bush = bush

    @property
    def tree(self):
        return self.__tree

    @tree.setter
    def quality(self, tree):
        self.__tree = tree

    @property
    def grass(self):
        return self.__grass

    @grass.setter
    def price(self, grass):
        self.__grass = grass

    @property
    def bush(self):
        return self.__bush

    @bush.setter
    def size(self, bush):
        self.__bush = bush
