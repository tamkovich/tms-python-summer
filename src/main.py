"""
Создать список фигур и в цикле
подсчитать и вывести площади всех фигур на экран
"""

from task_12.task_12_2 import Circle, Triangle, Square

circle1 = [[3, 4, 6], [5, 4, 3], [8, 7, 8]]
triangle1 = [[3, 4, 6, 2, 5, 9], [5, 4, 3, 1, 4, 6], [8, 7, 8, 4, 2, 7]]
square1 = [[3, 4, 7, 8], [5, 4, 1, 3], [8, 7, 6, -3]]

for i in circle1:
    circle = Circle(*i)
    print(circle.area_of_a_circle())

for i in triangle1:
    triangle = Triangle(*i)
    print(triangle.perimeter())

for i in square1:
    square = Square(*i)
    print(square.perimeter())
