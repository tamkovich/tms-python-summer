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
    output_list = []
    for i in args:
        output_list.append(i * 2)
    return output_list


random_numbs = [i for i in range(12)]
print(random_numbs)
print(m_to_sm(*random_numbs))
