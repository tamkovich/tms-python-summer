# Создать lambda функцию, которая принимает на вход неопределенное
# количество именных аргументов и выводит словарь с ключами удвоенной
# длины. {‘abc’: 5} -> {‘abcabc’: 5}


strings = {
    'abc': 5,
    'none': 12,
    'qr': 32,
}

func = lambda strings: {key + key: val for key, val in strings.items()}

print(func(strings))