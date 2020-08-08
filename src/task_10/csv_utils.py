import csv


def csv_writer(data, path):
    """
    Write data to a CSV file path
    """
    with open(path, "w") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(data)


def csv_reader(path, arg):
    """
    Read a csv file
    """
    rows = []
    with open(path, arg) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)
            rows.append(row)
        return 33 * "_"


def add_csv(path, data, position=-1):
    """
    Add data
    :param path: файл
    :param data: информация, для добавления в файл
    :param position: позиция добавления, по умолчанию последняя
    :return: ничего
    """
    rows = []
    with open(path, "r") as csvfile:
        for row in csv.reader(csvfile):
            rows.append(row)
    if position == -1:
        rows.append(data)
    else:
        rows.insert(position, data)

    with open(path, "w") as csvfile:
        for i in rows:
            csv.writer(csvfile).writerow(i)


def del_csv(path, position=-1):
    """
    Delete data
    :param path: файл
    :param position: позиция удаления
    :return: ничего
    """
    rows = []
    with open(path, "r") as csvfile:
        for row in csv.reader(csvfile):
            rows.append(row)

    del rows[position]

    with open(path, "w") as csvfile:
        for row in rows:
            csv.writer(csvfile).writerow(row)

def csv_sum(path, num_row: int) -> float:
    """
    Функция подсчета суммы в столбце
    :param path: файл
    :param num_row: номер столбца, сумму которого надо получить
    :return: сумма в столбце
    """

    rows = []
    with open(path) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            rows.append(row)
        total = 0
        for row in rows:
            if row[num_row].isdigit():
                total += float(row[num_row])
    return total


def max_csv(path, num_row):
    """
    Функция нахождения товара по максимальному значению заданного признака.
    задается столбец (ппризнак товара),
    в котором находится товар с максимальным значением
    :param path: файл
    :param num_row: номер столбца, в котором нужно найти максимум
    :return: значение максимума найденного товара.
    так же выводится наименование найденного товара
    """

    rows = []
    with open(path) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            rows.append(row)
        tmp = []
        for row in rows:
            if row[num_row].isdigit():
                tmp.append(row[num_row])
        mx = max(tmp)
    for row in rows:
        for i, el in enumerate(row):
            if el == mx:
                print(row[0])
    return mx

def min_csv(path, num_row):
    """
    Функция нахождения товара по минимальному значению заданного признака
    задается столбец (признак товара),
    в котором находится товар с минимальным значением
    :param path: файл
    :param num_row: номер столбца, в котором нужно найти минимум
    :return: значение минимума найденного товара.
    так же выводится наименование найденного товара
    """

    rows = []
    with open(path) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            rows.append(row)
        tmp = []
        for row in rows:
            if row[num_row].isdigit():
                tmp.append(row[num_row])
        mn = min(tmp)
    for row in rows:
        for i, el in enumerate(row):
            if el == mn:
                print(row[0])
    return mn

def csv_decrease(path, num_row: int, n=1):
    """
    Функция для уменьшения количества товара (по умеолчанию на 1)
    :param path: файл
    :param num_row: номер товара, который нужно уменьшить на один
    :param n: количество, на которое нужно уменьшить товар (по умолчанию 1)
    :return: обновленная таблица
    """

    rows = []
    with open(path) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            rows.append(row)
        if rows[num_row][1].isdigit():
            rows[num_row][1] = int(rows[num_row][1]) - n
        else:
            "Is no digit"
    return rows
