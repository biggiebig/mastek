import unittest
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../hscic'))
from hscic.newssearch import ArticleManager

class TestArticleManager(unittest.TestCase):
    """
        Unit Test Cases for ArticleManager
    """
    am = ArticleManager()

    def test_or_three_words(self):
        """
            Tests expected results searching articles using ArticleManager
            search function test condition: OR condition with 3 words
        """
        search_text = 'Care Quality Commission'
        search_type = 'OR'
        result = self.am.search_articles(search_text,search_type)
        self.assertEqual(result, ['0','1','2','3','4','5','6'])

    def test_or_three_words2(self):
        """
            Tests expected results searching articles using ArticleManager
            search function test condition: OR condition with 2 words
        """
        search_text = 'general population generally'
        search_type = 'OR'
        result = self.am.search_articles(search_text,search_type)
        self.assertEqual(result, ['6','8'])

    def test_or_month_year(self):
        """
            Tests expected results searching articles using ArticleManager
            search function test condition: OR condition with a year and month
        """
        search_text = 'September 2004'
        search_type = 'OR'
        result = self.am.search_articles(search_text,search_type)
        self.assertEqual(result, ['9'])

    def test_and_three_words(self):
        """
            Tests expected results searching articles using ArticleManager
            search function test condition: AND condition wwith three words
        """
        search_text = 'Care Quality Commission admission'
        search_type = 'AND'
        result = self.am.search_articles(search_text,search_type)
        self.assertEqual(result, ['1'])

    def test_and_three_words2(self):
        """
            Tests expected results searching articles using ArticleManager
            search function test condition: AND condition wwith three words
        """
        search_text = 'general population Alzheimer'
        search_type = 'AND'
        result = self.am.search_articles(search_text,search_type)
        self.assertEqual(result, ['6'])


if __name__ == '__main__':

    unittest.main()
