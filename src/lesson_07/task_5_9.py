# Для каждого натурального числа в промежутке от m до n вывести все делители,
# кроме единицы и самого числа. m и n вводятся с клавиатуры.

def find_all_dividers(x: int) -> list:
    """
    finds all dividers of number 'x' nd return a sorted list with them
    :param x: number for which dividers must found
    :return: sorted list of found dividers of number 'x'
    """
    dividers = []
    value = x
    i = 2
    while i <= value ** 0.5:
        if value % i == 0:
            dividers.append(i)
            if i * i != value:
                dividers.append(int(value / i))
        i += 1

    return sorted(dividers)


print(find_all_dividers(128))
