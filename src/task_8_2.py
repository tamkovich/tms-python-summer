a = ['qwert', 'wwd', 'wew']


def is_palindrome(string):
    reversed_string = string[::-1]
    return reversed_string == string


for i in a:
    if is_palindrome(i):
        print(f'"{i}" is palindrome')
