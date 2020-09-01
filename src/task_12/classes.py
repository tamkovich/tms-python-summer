"""
Создать класс Point, описывающий точку(атрибуты: x, y). Создать класс
Figure. Создать три дочерних класса Circle(атрибуты: координаты
центра(тип Point), длина радиуса; методы: нахождение периметра и
площади окружности), Triangle(атрибуты: три точки, методы: нахождение
площади и периметра), Square(атрибуты: две точки, методы: нахождение
площади и периметра). При потребности создавать все необходимые
методы не описанные в задании. Создать список фигур и в цикле
подсчитать и вывести площади всех фигур на экран[my-oop-03]
Примечание: в рамках задание создать два файла: classes.py и main.py.
В первом будут описаны все классы, во втором классы будут
импортированы и использованы.
"""


import math
import ABC


class Point:
    """Создан класс Точка"""
    def __init__(self, x: int, y: int):
        """
        координаты точки на плоскости
        :param x: координата x
        :param y: координата y
        """
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'


class Figure(ABC):
    """Создан класс Фигура"""


class Circle(Figure):
    """Создан класс Окружность"""
    def __init__(self, center_point: Point, R: int):
        """
        :param center_point: координаты центра окружности
        :param R: радиус целое число
        """
        self.center_point = center_point
        self.R = R  # радиус

    def perimeter(self):
        perimeter = 2 * math.pi * self.R
        return round(perimeter, 2)

    def area(self):
        area = math.pi * self.R ** 2
        return round(area, 2)


class Triangle(Figure):
    """Создан класс Треугольник"""
    def __init__(self, A: Point, B: Point, C: Point):
        """
        :param A: координаты первой вершины
        :param B: координаты 2 вершины
        :param C: координаты 3 вершины
        """
        self.A = A  # первая вершина
        self.B = B  # вторая вершина
        self.C = C  # третья вершина

    def perimeter(self):  # нахождение длин сторон треугольника
        side1 = math.sqrt((self.B.x-self.A.x)**2+(self.B.y-self.A.y)**2)
        side2 = math.sqrt((self.B.x-self.C.x)**2+(self.B.y-self.C.y)**2)
        side3 = math.sqrt((self.C.x-self.A.x)**2+(self.C.y-self.A.y)**2)
        perimeter = side1 + side2 + side3
        return round(perimeter, 2)

    def area(self):
        side1 = math.sqrt((self.B.x-self.A.x)**2+(self.B.y-self.A.y)**2)
        side2 = math.sqrt((self.B.x-self.C.x)**2+(self.B.y-self.C.y)**2)
        side3 = math.sqrt((self.C.x-self.A.x)**2+(self.C.y-self.A.y)**2)
        semi_p = (side1 + side2 + side3) / 2  # полупериметр
        area = math.sqrt(semi_p*(semi_p-side1)*(semi_p-side2)*(semi_p-side3))
        return round(area, 2)


class Square(Figure):
    """Создан класс Квадрат"""
    def __init__(self, A: Point, B: Point):
        """
        :param A: координаты первой вершины
        :param B: координаты 2 вершины
        """
        self.A = A  # первая вершина
        self.B = B  # вторая вершина

    def perimeter(self):
        side = math.sqrt((self.B.x-self.A.x)**2+(self.B.y-self.A.y)**2)
        perimeter = side * 4
        return round(perimeter, 2)

    def area(self):
        side = math.sqrt((self.B.x-self.A.x)**2+(self.B.y-self.A.y)**2)
        area = side * 2
        return round(area, 2)
