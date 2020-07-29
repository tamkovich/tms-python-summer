a = ['qwert', 'wwd', 'wew']


def is_palindrome(string: str) -> str:
    """
    Return True if string is palindrome
    :param string: input string
    :return: return boolean
    """
    return string[::-1] == string


for i in a:
    if is_palindrome(i):
        print(f'"{i}" is palindrome')
