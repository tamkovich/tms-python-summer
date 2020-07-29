"""Даны три слова. Выяснить, является ли хоть одно из них палиндромом
("перевертышем"), т. е. таким, которое читается одинаково слева направо и
справа налево. (Определить функцию, позволяющую распознавать слова
палиндромы.)"""

list_of_words = ["dog", "pop", "cat"]

def palindrome(word: str) -> str:
    return word[::-1]

for word in list_of_words:
    if words == palindrome(words):
        print(f"Это палиндром.\n{words} == {palindrome(words)}")
    else:
        print(f"Это не палиндром.\n{words} != {palindrome(words)}")
