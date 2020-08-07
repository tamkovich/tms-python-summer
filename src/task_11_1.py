"""Создать пять классов описывающие реальные объекты. Каждый класс
должен содержать минимум три приватных атрибута, конструктор, геттеры
и сеттеры для каждого атрибута, два метода."""

import math


class Circle:
    def __init__(self, x0=0, y0=0, r=0):
        """

        :param x0: center position of circle on x-axis
        :param y0: center position of circle on y-axis
        :param r: circle radius
        """
        self.__x0 = x0
        self.__y0 = y0
        self.__r = r

    @property
    def x0(self):
        return self.__x0

    @x0.setter
    def x0(self, x0):
        self.__x0 = x0

    @property
    def y0(self):
        return self.__y0

    @y0.setter
    def y0(self, y0):
        self.__y0 = y0

    @property
    def r(self):
        return self.__r

    @r.setter
    def r(self, r):
        if r > 0:

            self.__r = r
        else:
            self.__r = 0

    def get_area(self):
        return math.pi * self.__r ** 2

    def __repr__(self):
        return f'x0, y0: {self.__x0}, {self.__y0}; r = {self.__r}'


class Point:
    def __init__(self, x=0, y=0, z=0):
        self.__x = x
        self.__y = y
        self.__z = z

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y

    @property
    def z(self):
        return self.__z

    @y.setter
    def z(self, z):
        self.__z = z

    def length_to_center(self):
        return (self.__x ** 2 + self.__y ** 2 + self.__z ** 2) ** 0.5

    def __repr__(self):
        return f'x, y, z: {self.__x, self.__y, self.__z}'


class Cube:
    def __init__(self, center=Point(), length=0):
        self.__center = center
        self.__length = length
        self.__points()

    @property
    def center(self):
        return self.__center

    @center.setter
    def center(self, center):
        self.__center = center
        self.__points()

    @property
    def length(self):
        return self.length

    @length.setter
    def length(self, length):
        self.length = length
        self.__points()

    def __points(self):
        # z-axis is directed to us
        #                +y
        #                |
        #                |
        #       p2       |        p3                +z
        #                |                          | - top
        #                |                          |
        # -x ------------o------------- +x          |
        #                |(z)                       |
        #                |                          | - down
        #       p1       |        p4                -z
        #                |
        #                |
        #                -y
        self.__p_down1 = Point(
            self.__center.x - self.__length / 2,
            self.__center.y - self.__length / 2,
            self.__center.z - self.__length / 2)

        self.__p_down2 = Point(
            self.__center.x - self.__length / 2,
            self.__center.y + self.__length / 2,
            self.__center.z - self.__length / 2)

        self.__p_down3 = Point(
            self.__center.x + self.__length / 2,
            self.__center.y + self.__length / 2,
            self.__center.z - self.__length / 2)

        self.__p_down4 = Point(
            self.__center.x + self.__length / 2,
            self.__center.y - self.__length / 2,
            self.__center.z - self.__length / 2)

        self.__p_top1 = Point(
            self.__center.x - self.__length / 2,
            self.__center.y - self.__length / 2,
            self.__center.z + self.__length / 2)

        self.__p_top2 = Point(
            self.__center.x - self.__length / 2,
            self.__center.y + self.__length / 2,
            self.__center.z + self.__length / 2)

        self.__p_top3 = Point(
            self.__center.x + self.__length / 2,
            self.__center.y + self.__length / 2,
            self.__center.z + self.__length / 2)

        self.__p_top4 = Point(
            self.__center.x + self.__length / 2,
            self.__center.y - self.__length / 2,
            self.__center.z + self.__length / 2)

    def __repr__(self):
        return f'center: {self.__center};\n' \
               f'p_down1: {self.__p_down1};\n' \
               f'p_down2: {self.__p_down2};\n' \
               f'p_down3: {self.__p_down3};\n' \
               f'p_down4: {self.__p_down4};\n' \
               f'p_top1: {self.__p_top1};\n' \
               f'p_top2: {self.__p_top2};\n' \
               f'p_top3: {self.__p_top3};\n' \
               f'p_top4: {self.__p_top4};\n'


class Sphere:
    def __init__(self, center=Point(), r=0):
        self.__center = center
        self.__r = r
        self.__calc_volume()

    @property
    def center(self):
        return self.__center

    @center.setter
    def center(self, center):
        self.__center = center
        self.__calc_volume()

    @property
    def r(self):
        return self.__r

    @r.setter
    def r(self, r):
        self.__r = r
        self.__calc_volume()

    def __calc_volume(self):
        self.__volume = 4 * math.pi * (self.__r ** 3) / 3

    def __repr__(self):
        return f'center: {self.__center};\n' \
               f'r: {self.__r};\n' \
               f'volume: {self.__volume};'


class Pig:
    def __init__(self, name='Pyatochok', mass=50, age=1):
        self.__name = name
        self.__mass = mass
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def mass(self):
        return self.__mass

    @mass.setter
    def mass(self, mass):
        self.__mass = mass

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    def shit(self, shit_mass):
        print('The pig has taken a shit! His mass has reduced')
        self.__mass -= shit_mass

    def feed(self, food_mass):
        print('The Pig has eaten! His mass has reduced')
        self.__mass += food_mass

    def __repr__(self):
        return f'name: {self.__name};\n' \
               f'mass: {self.__mass};\n' \
               f'age: {self.__age};'


# testing
circle = Circle()
print(circle)
circle.r = 12.4
print(circle.get_area())
circle.x0 = 12
circle.y0 = 23
print(circle.x0)
print(circle)
print('=============')

p1 = Point()
print(p1)
p1.x = 2
p1.y = 3
p1.z = 5

print(p1)
print(p1.length_to_center())
print('++++++++++++++')

cube = Cube(Point(1, 1, 1), 2)
print(cube)
print(cube.center)

cube.center = Point(0, 0, 1)
print(cube)
print('++++++++++++++')

sphere = Sphere()
print(sphere)
sphere.r = 1
print(sphere)
print('++++++++++++++')

pig = Pig('Dirty pig')
print(pig)
