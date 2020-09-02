class A:
    def some_method(self):
        print('I am A')


class B:
    def some_method(self):
        print('I am B')


class C(A, B):
    def some_method(self):
        super().some_method()


c = C()
c.some_method()


class Pet:
    counter = 0

    def __init__(self):
        Pet.counter += 1

    def jump(self, meters):
        print(f'jump {meters} meters')

    def voice(self):
        pass


class Dog(Pet):
    def jump(self, meters):
        if meters > 0.5:
            print('dog cannot jump more 0.5 meters')
        else:
            super(Dog, self).jump(meters)

    def voice(self):
        print('Woof!')


class Cat(Pet):
    def jump(self, meters):
        if meters > 2:
            print('cat cannot jump more 2 meters')
        else:
            super(Dog, self).jump(meters)

    def voice(self):
        print('Meow!')


dog = Dog()
cat = Cat()

dog.jump(23)
dog.jump(0.1)

cat.voice()
dog.voice()

print(dir(cat))


class MyTime:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __ne__(self, other):
        return (self.hours != other.hours) or (self.minutes != other.minutes) or (self.seconds != other.seconds)

    def __eq__(self, other):
        return not self.__ne__(other)

    def __repr__(self):
        return f'{self.hours} : {self.minutes} : {self.seconds}'


t1 = MyTime(1, 3, 2)
t2 = MyTime(1, 30, 2)

t1 = t2

str = int
a = str('5')

int = MyTime

a = int(3,4,5)
print(a)
