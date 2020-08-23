# Создать декоратор для функции, которая принимает список чисел.
# Декоратор должен производить предварительную проверку данных -
# удалять все четные элементы из списка.

def delete_even_numbs(func):
    def odd_numbs(*input_list):
        output_list = []
        for i in input_list:
            if i % 2 != 0:
                output_list.append(i)
        return func(*output_list)

    return odd_numbs


def arg_reverse(func):
    def input_args(*args):
        output_list = list(args)
        output_list.reverse()
        return func(*output_list)

    return input_args


@arg_reverse
@delete_even_numbs
def m_to_sm(*args) -> list:
    output_list = [i * 2 for i in args]
    return output_list


random_numbs = [i for i in range(12)]
print(random_numbs)
print(m_to_sm(*random_numbs))
