def arg_reverse(func):
    def input_args(*args):
        output_list = list(args)
        output_list.reverse()
        return func(*output_list)
    return input_args


@arg_reverse
def test(a: list, b: int):
    return str(a), b


print(test([232], 3213))
