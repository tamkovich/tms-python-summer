class Apple:
    """
    __init__(self, ...) - DONE
    2 private attribute
    getter - DONE
    setter - DONE
    2 method public
    """

    def __init__(self, color, age):
        self.__color = color
        self.__age = age

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, apple_color):
        if apple_color != 'black':
            raise Exception('Invalid color')
        self.__color = apple_color

    @property
    def age(self):
        return self.__age


apple = Apple('red', 1)
# print(apple.color)
# print(apple.age)

apple.color = 'green'
print(apple.color)
