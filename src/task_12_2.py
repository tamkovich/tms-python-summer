"""
Создать класс Point, описывающий точку(атрибуты: x, y). Создать класс
Figure. Создать три дочерних класса Circle(атрибуты: координаты
центра(тип Point), длина радиуса; методы: нахождение периметра и
площади окружности), Triangle(атрибуты: три точки, методы: нахождение
площади и периметра), Square(атрибуты: две точки, методы: нахождение
площади и периметра). При потребности создавать все необходимые
методы не описанные в задании. Создать список фигур и в цикле
подсчитать и вывести площади всех фигур на экран[my-oop-03]
Примечание: в рамках задание создать два файла: classes.py и main.py. В
первом будут описаны все классы, во втором классы будут
импортированы и использованы.
"""

import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Figure:
    pass


class Circle(Figure):
    def __init__(self, x, y, r):
        self.point = Point(x, y)
        self.r = r

    def finding_the_perimeter(self):
        return 2 * math.pi * self.r

    def area_of_a_circle(self):
        return math.pi * self.r ** 2


class Triangle(Figure):
    def __init__(self, x1, x2, x3, y1, y2, y3):
        point1 = Point(x1, y1)
        point2 = Point(x2, y2)
        point3 = Point(x3, y3)
        self.line_a = ((point2.x - point1.x) ** 2 + (point2.y - point1.y) ** 2) ** 0.5
        self.line_b = ((point3.x - point2.x) ** 2 + (point3.y - point2.y) ** 2) ** 0.5
        self.line_c = ((point1.x - point3.x) ** 2 + (point1.y - point3.y) ** 2) ** 0.5

    def finding_the_perimeter(self):
        p = (self.line_a + self.line_b + self.line_c) / 2
        return math.sqrt(p * (p - self.line_a) * (p - self.line_b) * (p - self.line_c))

    def perimeter(self):
        return self.line_a + self.line_b + self.line_c


class Square(Figure):
    def __init__(self, x1, x2, y1, y2):
        point1 = Point(x1, y1)
        point2 = Point(x2, y2)
        self.line_a = ((point2.x - point1.x) ** 2 + (point2.y - point1.y) ** 2) ** 0.5

    def finding_the_perimeter(self):
        return self.line_a ** 2

    def perimeter(self):
        return 4 * self.line_a


