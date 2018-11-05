import re
from html.parser import HTMLParser


def extract_words_from_html(html):
    parser = WordsHTMLParser()
    parser.feed(html)

    return parser.words


class WordsHTMLParser(HTMLParser):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.words = []

    def handle_data(self, data):
        self.words.extend(re.findall(r'\w+', data))
