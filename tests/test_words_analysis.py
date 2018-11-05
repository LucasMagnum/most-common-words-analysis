import unittest

from words_analysis import get_most_common_words


class TestWordsAnalysis(unittest.TestCase):

    def test_get_most_common_words_should_return_the_expected_words(self):
        data = [
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

        expected = [
            ('python', 3),
            ('java', 2)
        ]

        most_common_words = get_most_common_words(data, 2)
        assert most_common_words == expected
