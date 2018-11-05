import unittest

from words_extractor import extract_words_from_html


class TestWordsExtractor(unittest.TestCase):

    def test_extract_words_from_webpage_should_return_the_expected_words(self):
        html = """
            <!DOCTYPE html>
            <html>
            <head>
                <title>Python language</title>
            </head>
            <body>
                <ul>
                    <li>python</li>
                    <li>ruby</li>
                    <li>java</li>
                    <li>python</li>
                    <li>earlang</li>
                    <li>java</li>
                    <li>golang</li>
                    <li>javascript</li>
                    <li>python</li>
                </ul>
            </body>
            </html>
        """

        expected_words = [
            'Python',
            'language',
            'python',
            'ruby',
            'java',
            'python',
            'earlang',
            'java',
            'golang',
            'javascript',
            'python'
        ]

        words = extract_words_from_html(html)
        assert sorted(words) == sorted(expected_words)
