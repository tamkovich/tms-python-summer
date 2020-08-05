'''
Создать декоратор для функции, которая принимает список чисел.
Декоратор должен производить предварительную проверку данных -
удалять все четные элементы из списка.
'''
my_list = [1, 28, 34, 15]
def decorator(func):
    def n_elents(*args):
        return func([i for i in args[0] if i % 2 !=0])
    return n_elents

@decorator
def my_func(x: list):
    print(x)
my_func(my_list)

