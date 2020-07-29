random_list = [i for i in range(67, 74)]
formated_list = lambda string: [f'{index} - {value}' for index, value in enumerate(string)]
print(random_list)
print(formated_list(random_list))
