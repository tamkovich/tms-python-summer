random_list = {'sds': 3, 'dsadf': 4, 'e4rwes': 5}
formated_list = lambda string: {key + key: string[key] for key in string}
print(random_list)
print(formated_list(random_list))
