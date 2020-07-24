# task_8_2
"""Даны три слова. Выяснить, является ли хоть одно из них палиндромом
("перевертышем"), т. е. таким, которое читается одинаково слева направо и
справа налево. (Определить функцию, позволяющую распознавать слова
палиндромы.)"""

list_of_words = ["dog", "pop", "cat"]


def is_palindrome(tmp: str) -> bool:
    """
    The function checks if the word is a palindrome
    :param tmp: word, which check
    :return: if palindrome - True, if not - False
    """
    return tmp == tmp[::-1]


for word in list_of_words:
    print(f"Word: {word}. Palindrome: {word[::-1]}")
    if is_palindrome(word):
        print("It's good.")
    else:
        print("It's not good.")
