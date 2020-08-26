from random import randint


class Matrix:

    def __init__(self, *args) -> None:
        arg_len = len(args)
        if arg_len == 0:
            self.__n = 5
            self.__m = 5
            self.__data = []
            self.__data = [[0 for i in range(self.__n)] for j in range(self.__m)]
        elif arg_len == 3:
            self.__n = args[0]
            self.__m = args[1]
            self.__a = args[2][0]
            self.__b = args[2][1]
            self.__data = []
            self.__fill_random_el()
        elif arg_len == 1 and type(args[0]) == Matrix:
            self.__n = args[0].__n
            self.__m = args[0].__m
            self.__data = args[0].__data
        else:
            raise Exception('Invalid data: incorrect number of parameters')

    def __fill_random_el(self):
        self.__data = [[randint(self.__a, self.__b) for i in range(self.__n)] for j in range(self.__m)]

    def __str__(self):
        result = []
        for i in self.__data:
            result.append(str(i) + '\n')
        result = ''.join(result)
        return result

    @property
    def data(self):
        return self.__data


if __name__ == '__main__':
    m1 = Matrix()
    print(str(m1))
