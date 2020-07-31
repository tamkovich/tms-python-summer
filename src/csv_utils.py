import csv


def csv_read(file_name):
    """
    Read a csv file
    """
    with open(file_name, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        rows = []
        for row in csv_reader:
            rows.append(row)
        return rows


def csv_writer(data, path):
    """
    Write data to a CSV file path
    """
    with open(path, "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)


def csv_position_write(data, file_name, line=False, column=False):
    """
    add value by position a csv file
    """
    with open(file_name, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        rows = []
        for row in csv_reader:
            rows.append(row)
    if line is False and column is False:
        rows.append(data)
    elif line is False:
        rows.insert(column, data)
    elif column is False:
        rows.insert(line, data)
    else:
        tmp = rows[line]
        tmp.insert(column, data)
        rows[line] = tmp
    with open(file_name, "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for lines in rows:
            writer.writerow(lines)


def csv_position_delete(file_name=None, line=False, column=False):
    """
    delete value by position a csv file
    """
    with open(file_name, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        rows = []
        for row in csv_reader:
            rows.append(row)
    if line is False and column is False:
        rows.pop()
    elif line is False:
        rows.pop(column)
    elif column is False:
        rows.pop(line)
    else:
        tmp = rows[line]
        tmp.pop(column)
        rows[line] = tmp
    with open(file_name, "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for lines in rows:
            writer.writerow(lines)


def csv_sum_price(file_name):
    """
    sum of all goods
    """
    with open(file_name, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        sum_price = 0
        for row in reader:
            sum_price += int(row['price'])
    return sum_price


def search_max_price(file_name):
    """
    search max price
    """
    with open(file_name, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        sum_price = []
        for row in reader:
            sum_price.append(int(row['price']))
    return max(sum_price)


def search_min_price(file_name):
    """
    search min price
    """
    with open(file_name, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        sum_price = []
        for row in reader:
            sum_price.append(int(row['price']))
    return min(sum_price)


def decrease_quantity(file_name=None, quantity=1):
    """
    decrease in the quantity of goods
    """
    with open(file_name, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        rows = []
        for row in csv_reader:
            rows.append(row)
        for i in range(quantity):
            del rows[-1]
    with open(file_name, "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for lines in rows:
            writer.writerow(lines)
