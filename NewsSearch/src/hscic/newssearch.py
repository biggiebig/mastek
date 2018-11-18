from collections import namedtuple
import uuid

Article = namedtuple('Article', 'id ref contents article_type')


class ArticleManager:
    """
    ArticleManager: Retrieves and search articles. articles are pre-loaded from a file defined in .config file
    """
    __article_path = 'Articles.txt'
    __news_articles = []

    def __init__(self):
        self.__load_articles()

    def __load_articles(self):
        # TODO Load articles files location from config file,
        # Creating a uniqueid for id field , can be read from DB for future use
        try:
            with open(self.__article_path, 'r') as article_file:
                for i, article in enumerate(article_file.readlines()):
                    self.__news_articles.\
                            append(
                                Article(
                                        id = uuid.uuid1(),
                                        ref=str(i),
                                        contents=article,
                                        article_type='News'
                                        ))
        except Exception as e:
            # Print for now can be extended to log error
            print(f'An error in load_articles: {e}')
            raise

    def get_articles(self):
        """
           Returns a enumerator for each of the articles in the pre-loaded articles collection
        """
        try:
            for news_article in self.__news_articles:
                yield news_article
        except Exception as e:
                # Print for now can be extended to log error
                print(f'An error in get_articles: {e}')
                raise

    def search_articles(self, search_keywords, search_type='AND'):
        """
            searches the pre-loaded articles for the provided search parameter and condition
            Parameters
            ----------
            search_keyword : str
                List of words to search
            search_type : str
                Type of search to perform valid values (OR,AND)
        """
        try:
            article_names = set([])
            search_words = search_keywords.split()
            for news_article in self.__news_articles:
                id, ref, contents, article_type = news_article
                if search_type.upper() == 'AND':
                    if(ArticleHelperFunctions.find_text_and
                        (search_words,
                         contents
                         )):
                        article_names.add(ref)
                else:
                    if(ArticleHelperFunctions.find_text_or(
                        search_words,
                        contents
                    )):
                        article_names.add(ref)
            return sorted(list(article_names))
        except Exception as e:
                print(f'An error in search_articles: {e}')
                raise


class ArticleHelperFunctions:
    """
        A utility class to provide basic search functionality
    """
    @staticmethod
    def find_text_or(search_keywords, article_contents):
        """
            Search all the words in keywords within the article contents
            using OR statement.Returns TRUE or FALSE
            Parameters
            ----------
            article_contents : str
             List of words to search
            search_keywords : list
             Contents of article to search
        """
        for keyword in search_keywords:
            if article_contents.find(keyword) != -1:
                'Found one of the keywords so return when found'
                return True
        return False

    @staticmethod
    def find_text_and(search_keywords, article_contents):
        """
            Search all the words in keywords within the article contents
            using AND statement.Returns TRUE or FALSE
            Parameters
            ----------
            article_contents : str
            List of words to search
            search_keywords : list
            Contents of article to search
        """
        found_text = list(filter(
                                lambda x: article_contents.find(x) != -1,
                                search_keywords
                                ))
        '#If the filtered length is the same we return true as all keywords have been found'
        return len(found_text) == len(search_keywords)
