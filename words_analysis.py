from collections import Counter


def get_most_common_words(words, number):
    counter = Counter(words)
    return counter.most_common(number)
