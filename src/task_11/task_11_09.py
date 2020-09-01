"""
Создать три класса: Dog, Cat, Parrot.
Атрибуты каждого класса: name, age, master.
Каждый класс содержит конструктор и методы:
run, jump, birthday(увеличивает age на 1), sleep.
Класс Parrot имеет дополнительный метод fly.
Cat - meow, Dog - bark.
"""


class Dog:
    """создан класс Собака"""

    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def bark(self):
        print(f'{self.name} said: "Woof woof!"')

    def run(self):
        print(f'{self.name} run')

    def jump(self):
        print(f'{self.name} jump')

    def sleep(self):
        print(f'{self.name} sleep')

    def birthday(self):
        self.age += 1
        print(f'Today {self.name} turns {self.age} old')


class Cat:
    """создан класс Кот"""

    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def meow(self):
        print(f'{self.name} said: "meow!"')

    def run(self):
        print(f'{self.name} run')

    def jump(self):
        print(f'{self.name} jump')

    def sleep(self):
        print(f'{self.name} sleep')

    def birthday(self):
        self.age += 1
        print(f'Today {self.name} turns {self.age} old')


class Parrot:
    """создан класс Попугай"""

    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def fly(self):
        print(f'{self.name} fly')

    def run(self):
        print(f'{self.name} run')

    def jump(self):
        print(f'{self.name} jump')

    def sleep(self):
        print(f'{self.name} sleep')

    def birthday(self):
        self.age += 1
        print(f'Today {self.name} turns {self.age} old')


dog1 = Dog('Fox', 13, 'Minsk')
dog1.sleep()
dog1.run()
dog1.birthday()
print(dog1.age)
dog1.bark()
print(dog1.master)
dog1.birthday()
