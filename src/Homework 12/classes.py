# task_12_2
"""Создать класс Point, описывающий точку(атрибуты: x, y). Создать класс
Figure. Создать три дочерних класса Circle(атрибуты: координаты
центра(тип Point), длина радиуса; методы: нахождение периметра и
площади окружности), Triangle(атрибуты: три точки, методы: нахождение
площади и периметра), Square(атрибуты: две точки, методы: нахождение
площади и периметра). При потребности создавать все необходимые
методы не описанные в задании. Создать список фигур и в цикле
подсчитать и вывести площади всех фигур на экран
Примечание: в рамках задание создать два файла:  classes.py  и main.py.
В первом будут описаны все классы, во втором классы будут
импортированы и использованы."""
import math
import abc


class Point:
    """
    Class describes point with coordinates x and y
    """

    def __init__(self, x: float, y: float):
        """
        Constructor of class point
        :param x: point coordinate x
        :param y: point coordinate y
        """
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        """
        Print coordinates in correct format
        :return: str
        """
        return f"{self.x, self.y}"


class Figure(abc.ABC):
    """
    Interface
    """

    @abc.abstractmethod
    def perimeter(self):
        """
        Calculate perimeter of some figure
        :return: exception
        """
        raise NotImplemented

    @abc.abstractmethod
    def area(self):
        """
        Calculate area of some figure
        :return: exception
        """
        raise NotImplemented


class Circle(Figure):
    """
    Describes some attributes and methods of the circle
    """

    def __init__(self, center: Point, radius: float):
        """
        Center coordinates and radius of the circle
        :param center: center coordinates of the circle
        :param radius: radius of the circle
        """
        self.center = center
        self.radius = radius

    def perimeter(self) -> float or str:
        """
        Calculate perimeter of circle
        :return: perimeter or mistake
        """
        try:
            return 2 * self.radius * math.pi
        except ValueError:
            return f"Mistake"

    def area(self) -> float or str:
        """
        Calculate area of circle
        :return: area or mistake
        """
        try:
            return math.pi * self.radius ** 2
        except ValueError:
            return f"Mistake"


class Triangle(Figure):
    """
    Describes some attributes and methods of the triangle
    """

    def __init__(self, point_1: Point, point_2: Point, point_3: Point):
        """
        Three tops of triangle
        :param point_1: first top of triangle
        :param point_2: second top of triangle
        :param point_3: third top of triangle
        """
        self.side_1 = side_of_figure(point_1, point_2)
        self.side_2 = side_of_figure(point_1, point_3)
        self.side_3 = side_of_figure(point_2, point_3)

    def perimeter(self) -> float or str:
        """
        Calculate perimeter of triangle
        :return: perimeter of mistake
        """
        try:
            return sum([self.side_1, self.side_2, self.side_3])
        except ValueError:
            return f"Mistake"

    def area(self) -> float or str:
        """
        Calculate area of triangle
        :return: area or mistake
        """
        semi_p = self.perimeter() / 2
        try:
            return math.sqrt(
                semi_p
                * (semi_p - self.side_1)
                * (semi_p - self.side_2)
                * (semi_p - self.side_3)
            )
        except ValueError:
            return f"Mistake"


class Square(Figure):
    """
    Describes some attributes and methods of the square
    """

    def __init__(self, point_1: Point, point_2: Point):
        """
        Top coordinates of the square
        :param point_1: first point
        :param point_2: second point
        """
        self.side = side_of_figure(point_1, point_2)

    def perimeter(self) -> float or str:
        """
        Calculate perimeter of square
        :return: perimeter or mistake
        """
        try:
            return 4 * self.side
        except ValueError:
            return f"Mistake"

    def area(self) -> float or str:
        """
        Calculate area of square
        :return: area or mistake
        """
        try:
            return self.side ** 2
        except ValueError:
            return f"Mistake"


def side_of_figure(p1: Point, p2: Point):
    """
    Calculate side of figure
    :param p1: first point
    :param p2: second point
    :return: side
    """
    return math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)
