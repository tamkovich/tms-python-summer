class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Figure:
    pass


class Circle(Figure):
    def __init__(self, radius, center):
        self.center = center
        self.radius = radius

    def area(self):
        area = 3.14 * (self.radius ** 2)
        return area

    def perimetr(self):
        perimetr = 2 * 3.14 * self.radius
        return perimetr


class Triangle(Figure):
    def __init__(self, point_1, point_2, point_3):
        self.point_1 = point_1
        self.point_2 = point_2
        self.point_3 = point_3

    def perimetr(self):
        side1 = ((self.point_1.x - self.point_2.x) ** 2 + (self.point_1.y - self.point_2.y) ** 2) ** 0.5
        side2 = ((self.point_2.x - self.point_3.x) ** 2 + (self.point_2.y - self.point_3.y) ** 2) ** 0.5
        side3 = ((self.point_3.x - self.point_1.x) ** 2 + (self.point_3.y - self.point_1.y) ** 2) ** 0.5
        perimetr = side1 + side2 + side3
        return perimetr

    def area(self):
        area = abs(((self.point_2.x - self.point_1.x) * (self.point_3.y - self.point_1.y) - (
                self.point_3.x - self.point_1.x) * (self.point_2.y - self.point_1.y)) * 0.5)
        return area


class Square(Figure):
    def __init__(self, point_1, point_2):
        self.point_1 = point_1
        self.point_2 = point_2

    def perimetr(self):
        perimetr = (abs(self.point_2.x - self.point_1.x) + abs(self.point_2.y - self.point_1.y)) * 2
        return perimetr

    def area(self):
        area = abs(self.point_2.x - self.point_1.x) * abs(self.point_2.y - self.point_1.y)
        return area
