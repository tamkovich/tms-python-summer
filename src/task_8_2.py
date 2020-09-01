# Даны три слова. Выяснить, является ли хоть одно из них палиндромом
# ("перевертышем"), т. е. таким, которое читается одинаково слева направо и
# справа налево. Определить функцию, позволяющую распознавать слова
# палиндромы.

def is_palindrome(word: str) -> bool:
    """
    return true if 'word' is a palindrome or empty and false when 'word' isn't a palindrome;
    :param word: string
    :return: bool
    """
    return word == word[::-1]


# testing

print(f'\'aabaa\' - {is_palindrome("aabaa")}')
print(f'\'aabbaa\' - {is_palindrome("aabbaa")}')
print(f'\'asdabbadsa\' - {is_palindrome("asdabbadsa")}')

print(f'\'\' - {is_palindrome("")}')
