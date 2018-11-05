from collections import Counter


def get(words, number):
    counter = Counter(words)
    return counter.most_common(number)
