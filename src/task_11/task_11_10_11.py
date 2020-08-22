"""
Создать родительский класс Pet,
содержащий все общие методы классов Dog, Cat, Parrot.
Унаследовать Dog, Cat, Parrot от класса Pet.
Удалить в дочерних классах те методы,
которые имеются у родительского класса.
Создать объект каждого класса и вызвать все его методы.
"""

"""
Добавить два новых атрибута в родительский класс: weight и height.
Добавить методы change_weight, change_height 
принимающий один параметр и прибавляющий его к соответствующему аргументу. 
В случае если параметр не был передан, увеличивать на 0.2.
Изменить метод fly класса Parrot. 
Если вес больше 0.1 выводить сообщение This parrot cannot fly.
"""

class Pet:
    """создан класс Питомец"""

    def __init__(self, name, age, master, weight, height):
        self.name = name
        self.age = age
        self.master = master
        self.weight = weight
        self.height = height

    def run(self):
        print(f'{self.name} run')

    def jump(self):
        print(f'{self.name} jump')

    def sleep(self):
        print(f'{self.name} sleep')

    def birthday(self):
        self.age += 1
        print(f'Today {self.name} turns {self.age} old')

    def change_weight(self, change_weight=0.2):
        self.weight += change_weight

    def change_height(self, change_height):
        self.height += change_height

class Dog(Pet):
    """создан класс Собака"""

    def bark(self):
        print(f'{self.name} said: "Woof woof!"')

class Cat(Pet):
    """создан класс Кот"""

    def meow(self):
        print(f'{self.name} said: "meow!"')

class Parrot(Pet):
    """создан класс Попугай"""

    def fly(self):
        if self.weight > 0.1:
            print(F"{self.name} cannot fly")
        else:
            print(f'{self.name} fly')


dog1 = Dog("Rex", 5, "Good", 6, 30)
cat1 = Cat("Barsik", 10, "Normal", 3, 20)
parrot1 = Parrot("Vasia", 15, "Best", 0.1, 10)

print(dog1.__dict__)
dog1.sleep()
dog1.run()
dog1.jump()
dog1.bark()
dog1.birthday()
dog1.change_height(2)
print(dog1.height)

print(cat1.__dict__)
cat1.sleep()
cat1.run()
cat1.jump()
cat1.meow()
cat1.birthday()
cat1.change_weight(-0.2)
print(cat1.weight)

print(parrot1.__dict__)
parrot1.sleep()
parrot1.run()
parrot1.jump()
parrot1.fly()
parrot1.birthday()
parrot1.change_weight()
parrot1.fly()
print(round(parrot1.weight, 2))
