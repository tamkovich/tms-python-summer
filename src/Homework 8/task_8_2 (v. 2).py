# task_8_2
"""Даны три слова. Выяснить, является ли хоть одно из них палиндромом
("перевертышем"), т. е. таким, которое читается одинаково слева направо и
справа налево. (Определить функцию, позволяющую распознавать слова
палиндромы.)"""

list_of_words = ["dog", "pop", "cat"]


def is_palindrome(tmp: str) -> str:
    """
    The function make a palindrome
    :param tmp: Some word
    :return: Palindrome of param
    """
    return tmp[::-1]


for word in list_of_words:
    if word == is_palindrome(word):
        print(f"It's a palindrome.\n{word} == {is_palindrome(word)}")
    else:
        print(f"It's not a palindrome.\n{word} != {is_palindrome(word)}")
