def find_max_matrix_element(matrix) -> int or float:
    matrix = matrix.data
    max_elem_string = []
    for i in matrix:
        x = max(i)
        max_elem_string.append(x)

    max_elem = max(max_elem_string)
    counter = 0
    for i in matrix:
        for j in i:
            if j == max_elem:
                counter += 1
    if counter == 1:
        for i in matrix:
            if max_elem in i:
                pos_max_elem = i.index(max_elem) + 1
                pos_spis = matrix.index(i) + 1
        print(f'максимальный элемент матрицы: {max_elem}, позиция: [{pos_spis}][{pos_max_elem}]')
    else:
        print(f'максимальный элемент матрицы: {max_elem}, таких элементов несколько')
    return max_elem


def find_min_matrix_element(matrix) -> int or float:
    matrix = matrix.data
    max_elem_string = []
    for i in matrix:
        x = min(i)
        max_elem_string.append(x)

    min_elem = min(max_elem_string)
    counter = 0
    for i in matrix:
        for j in i:
            if j == min_elem:
                counter += 1
    if counter == 1:
        for i in matrix:
            if min_elem in i:
                pos_min_elem = i.index(min_elem) + 1
                pos_spis = matrix.index(i) + 1
        print(f'минимальный элемент матрицы: {min_elem}, позиция: [{pos_spis}][{pos_min_elem}]')
    else:
        print(f'минимальный элемент матрицы: {min_elem}, таких элементов несколько')
    return min_elem


def find_sum_matrix_elements(matrix) -> int or float:
    matrix = matrix.data
    sum_string = []
    for i in matrix:
        x = sum(i)
        sum_string.append(x)

    sum_elem = sum(sum_string)
    print(f'сумма всех элементов матрицы: {sum_elem}')
    return sum_elem
