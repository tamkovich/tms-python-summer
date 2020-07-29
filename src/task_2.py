random_list = {'sds': 3, 'dsadf': 4, 'e4rwes': 5}
print(random_list)
print((lambda string: {key + key: string[key] for key in string})(random_list))
