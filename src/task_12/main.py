import classes

circle = classes.Circle(classes.Point(1, 1), 25)
triangle = classes.Triangle(
    classes.Point(1, 1), classes.Point(4, 5), classes.Point(9, 11)
)

square = classes.Square(classes.Point(2, 8), classes.Point(5, 9))
list_of_figures = [circle, triangle, square]

for i, el in enumerate(list_of_figures):
    print(f'area {i} = {el.area()}')
