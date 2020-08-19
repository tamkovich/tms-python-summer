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
import classes

list_of_figures = []

point_1 = classes.Point(10, 10)
point_2 = classes.Point(20, 20)
point_3 = classes.Point(10, 20)

list_of_figures.append(circle := classes.Circle(point_2, 10))
print(f"Circle center: {circle.center}")
print(f"Circle perimeter: {circle.perimeter()}\n")

list_of_figures.append(triangle := classes.Triangle(point_1, point_2, point_3))
print(f"Triangle sides: {triangle.side_1}, {triangle.side_2}, {triangle.side_3}")
print(f"Triangle perimeter: {triangle.perimeter()}\n")

list_of_figures.append(square := classes.Square(point_1, point_2))
print(f"Square sides: {square.side}")
print(f"Square perimeter: {square.perimeter()}\n")

for figure in list_of_figures:
    print(f"{figure} area: {figure.area()}")
