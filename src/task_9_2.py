# Создать lambda функцию, которая принимает на вход неопределенное
# количество именных аргументов и выводит словарь с ключами удвоенной
# длины. {‘abc’: 5} -> {‘abcabc’: 5}


random_dict = {'sds': 3, 'dsadf': 4, 'e4rwes': 5}
print(random_dict)
func = lambda string: {key + key: value for key, value in string.items()}
print(func(random_dict))
