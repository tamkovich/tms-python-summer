"""Создать класс Point, описывающий точку(атрибуты: x, y). Создать класс
Figure. Создать три дочерних класса Circle(атрибуты: координаты
центра(тип Point), длина радиуса; методы: нахождение периметра и
площади окружности), Triangle(атрибуты: три точки, методы: нахождение
площади и периметра), Square(атрибуты: две точки, методы: нахождение
площади и периметра). При потребности создавать все необходимые
методы не описанные в задании. Создать список фигур и в цикле
подсчитать и вывести площади всех фигур на экран[my-oop-03]
Примечание: в рамках задание создать два файла: ​ classes.py ​ и m
​ ain.py ​ . В
первом будут описаны все классы, во втором классы будут
импортированы и использованы."""

import math


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __lt__(self, other):
        return self.__x ** 2 + self.__y ** 2 < other.__x ** 2 + other.__y ** 2

    def distance_to_center(self):
        return (self.__x ** 2 + self.__y ** 2) ** 0.5

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) == int or type(x) == float:
            self.__x = x
        else:
            raise Exception('x: invalid type')

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) == int or type(y) == float:
            self.__y = y
        else:
            raise Exception('y: invalid type')


class Figure:
    def get_perimeter(self):
        pass

    def get_area(self):
        pass


class Circle(Figure):
    def __init__(self, center=Point(), r=0):
        self.center = center
        self.r = r

    def __repr__(self):
        return 'Circle'

    @property
    def center(self):
        return self.__center

    @center.setter
    def center(self, center):
        if type(center) == Point:
            self.__center = center
        else:
            raise Exception('type of attribute center must be Point')

    @property
    def r(self):
        return self.__r

    @r.setter
    def r(self, r):
        if type(r) == int or type(r) == float:
            self.__r = r
        else:
            raise Exception('type of attribute r must be float or int')

    def get_perimeter(self):
        return 2 * math.pi * self.__r

    def get_area(self):
        return math.pi * self.__r ** 2


class Triangle(Figure):
    def __init__(self, points):
        self.__points = []
        self.points = points
        if not self.__is_triangle(self.__points):
            raise Exception('triangle cannot consist of such points')

    def __repr__(self):
        return 'Triangle'

    @property
    def points(self):
        return self.__points

    @points.setter
    def points(self, points):
        if len(points) != 3:
            raise Exception('args length is not equal 3')
        for i in range(3):
            if type(points[i]) == Point:
                self.__points.append(points[i])
            else:
                raise Exception(f'type of args[{i}] is not Point')

    def __get_length(self, points):
        return ((points[0].x - points[1].x) ** 2 + (points[0].y - points[1].y) ** 2) ** 0.5

    def __is_triangle(self, points):
        a = self.__get_length(self.__points[:2])
        b = self.__get_length(self.__points[1:3])
        c = self.__get_length(self.__points[:3:2])
        return ((a + b) > c) and \
               ((a + c) > b) and \
               ((b + c) > c)

    def get_perimeter(self):
        return self.__get_length(self.__points[:2]) + \
               self.__get_length(self.__points[1:3]) + \
               self.__get_length(self.__points[:3:2])

    def get_area(self):
        a = self.__get_length(self.__points[:2])
        b = self.__get_length(self.__points[1:3])
        c = self.__get_length(self.__points[:3:2])
        p = (a + b + c) * 0.5
        return (p * (p - a) * (p - b) * (p - c)) ** 0.5


class Square(Figure):
    def __init__(self, points):
        self.__points = []
        self.points = points

        self.__r1 = Point(points[1].x - points[0].x, points[1].y - points[0].y)
        self.__r2 = Point(points[2].x - points[1].x, points[2].y - points[1].y)
        self.__r3 = Point(points[0].x - points[2].x, points[0].y - points[2].y)

        if not self.__is_square(self.points):
            raise Exception('square cannot consist of such points')

    def __repr__(self):
        return 'Square'

    @property
    def points(self):
        return self.__points

    @points.setter
    def points(self, points):
        if len(points) != 3:
            raise Exception('args length is not equal 3')
        for i in range(3):
            if type(points[i]) == Point:
                self.__points.append(points[i])
            else:
                raise Exception(f'type of args[{i}] is not Point')

    def __is_square(self, points):
        if (self.__r1.x * self.__r2.x + self.__r1.y * self.__r2.y == 0) and (
                self.__r1.x ** 2 + self.__r1.y ** 2 == self.__r2.x ** 2 + self.__r2.y ** 2):
            return True

        if (self.__r3.x * self.__r2.x + self.__r3.y * self.__r2.y == 0) and (
                self.__r3.x ** 2 + self.__r3.y ** 2 == self.__r2.x ** 2 + self.__r2.y ** 2):
            return True

        if (self.__r3.x * self.__r1.x + self.__r3.y * self.__r1.y == 0) and (
                self.__r3.x ** 2 + self.__r3.y ** 2 == self.__r1.x ** 2 + self.__r1.y ** 2):
            return True

        return False

    def get_perimeter(self):
        a = min(self.__r1, self.__r2, self.__r3)
        return 4 * a.distance_to_center()

    def get_area(self):
        return min(self.__r1, self.__r2, self.__r3).distance_to_center() ** 2


# testing

if __name__ == '__main__':
    p1 = Point(0, 2)

    circle1 = Circle(p1, 1)
    print(circle1.get_perimeter(), circle1.get_area())

    triangle1 = Triangle((Point(0, 0),
                          Point(3, 0),
                          Point(0, 4),))

    print(triangle1.get_perimeter())
    print(triangle1.get_area())

    square1 = Square(
        (Point(0, 0),
         Point(3, 4),
         Point(-1, 7),))

    print(square1.get_perimeter())
    print(square1.get_area())

    list_of_figures = []
    for i in range(1, 5):
        list_of_figures.append(Circle(Point(i, i), 3 * i))
        list_of_figures.append(Triangle(
            (Point(i, i),
             Point(i, 5 * i),
             Point(5 * i, i))
        ))
        list_of_figures.append(Square(
            (Point(i, i),
             Point(i, 5 * i),
             Point(5 * i, i))
        ))

    for i in list_of_figures:
        print(f'{i}: Area is {i.get_area()}')
