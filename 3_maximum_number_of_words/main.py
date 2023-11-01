"""
Вам дан список предложений.
предложения содержит только слова, которые разделены единичными пробелами.
Необзодимо вернуть максимальное количество слов, которое содержится в одном предложении.
sentences[i] - это одно предложение.
Если ни одно из предложений не содержит слов, то нужно вернуть 0
Проверка:
pytest ./3_maximum_number_of_words/test.py
"""


def get_max_number_of_words_from_sentences(sentences: list[str]) -> int:
    max_len = 0
    for sentence in sentences:
        if len(sentence.split(' ')) > max_len and len(sentence) > 0:
            max_len = len(sentence.split(' '))
    return max_len

print(get_max_number_of_words_from_sentences(["alice and bob love cats", "i think so too", "this is great thanks very much"]))
print(get_max_number_of_words_from_sentences(["please wait", "continue to fight", "continue to win"]))
print(get_max_number_of_words_from_sentences(['', '']))