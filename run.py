import argparse
import os

import requests

from words_analysis import get_most_common_words
from words_extractor import extract_words_from_html


LINKS_PATH = "links/"


def get_words(case_sensitive=False):
    words = []

    for link in get_links():
        html = get_html(link)
        html_words = extract_words_from_html(html.decode("utf-8"))

        if not case_sensitive:
            html_words = map(str.lower, html_words)

        words.extend(html_words)

    return words


def get_html(link):
    response = requests.get(link)
    return response.content


def get_links():
    links = []

    for textfile in os.listdir(LINKS_PATH):
        filename = f"{LINKS_PATH}{textfile}"

        with open(filename) as file:
            links.extend([link.strip() for link in file.readlines()])

    return links


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Extract the most common words from a list of links'
    )
    parser.add_argument('number_of_words', metavar='n', type=int,
                        help='an integer number of words')

    args = parser.parse_args()
    words = get_words()

    print(get_most_common_words(words, args.number_of_words))
