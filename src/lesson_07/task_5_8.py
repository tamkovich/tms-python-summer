# В заданной строке расположить в обратном порядке все слова. Разделителями
# слов считаются пробелы.

sentence = "В заданной строке расположить в обратном порядке все" \
           " слова. Разделителями слов считаются пробелы."


def reverser(sentence: str) -> str:
    """
    return reversed words in 'sentence'
    :param sentence: string contains sentence
    :return: sentence with words in reversed position
    """
    words = sentence.split(' ')
    print(words)
    words.reverse()

    return ' '.join(words)


print(reverser(sentence))
