"""
 Создать класс Point, описывающий точку(атрибуты: x, y).
Создать класс Figure. Создать три дочерних класса Circle(атрибуты: координаты центра(тип Point),
длина радиуса; методы: нахождение периметра и площади окружности),
Triangle(атрибуты: три точки, методы: нахождение площади и периметра),
Square(атрибуты: две точки, методы: нахождение площади и периметра).
При потребности создавать все необходимые методы не описанные в задании.
 Создать список фигур и в цикле подсчитать и вывести площади всех фигур на экран
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Figure:
    pass


from math import pi


class Circle(Figure):
    def __init__(self, x_centre, y_center, radius):
        self.x_center = x_centre
        self.y_center = y_center
        self.radius = radius

    def area(self):
        s = self.radius ** 2 * pi
        return s

    def perimeter(self):
        p = self.radius * 2 * pi
        return p


class Triangle(Figure):
    def __init__(self, x1, x2, x3, y1, y2, y3):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.y1 = y1
        self.y2 = y2
        self.y3 = y3
        self.line1 = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        self.line2 = ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5
        self.line3 = ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** 0.5

    def area(self):
        tr_s = self.line1 * self.line2 * 0.5
        return tr_s

    def perimeter(self):
        per = self.line1 + self.line2 + self.line3
        return per


class Square(Figure):
    def __init__(self, xs1, xs2, ys1, ys2):
        self.xs1 = xs1
        self.xs2 = xs2
        self.ys1 = ys1
        self.ys2 = ys2
        self.sq_line = ((xs2 - xs1) ** 2 + (ys2 - ys1) ** 2) ** 0.5

    def area(self):
        sq = self.sq_line ** 2
        return sq

    def perimeter(self):
        sp = self.sq_line * 4
        return sp


square1 = Square(12, 32, 7, 3)
triangle1 = Triangle(1, 32, 12, 3, 2, 11)
round1 = Circle(12, 21, 4)
square2 = Square(14, 21, 4, 2)
triangle2 = Triangle(0, 11, 3, -4, 22, 1)
some_circle = Circle(12, 34, 11)
list_of_figures = [triangle1, round1, square2, triangle2, some_circle]
for figure in list_of_figures:
    print(figure.area())
