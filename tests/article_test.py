import unittest
from models import news
News = news.News

class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Article class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Article('abcnews')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))


if __name__ == '__main__':
    unittest.main()