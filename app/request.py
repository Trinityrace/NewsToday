
import urllib.request, json
#from .models import news
from .models import News, Articles

# News = news.News
# # Getting api key
# api_key = app.config['64281a2732dd4fbba93a0ce3e0352cc5']
# # Getting the news base url
# base_url = app.config['https://newsapi.org/v2/top-headlines?'
#        'country=us&']

api_key = None
news_url = None
articles_url = None
topheadlines_url = None
everything_url = None
everything_search_url = None

def configure_request(app):
    global api_key, base_url, articles_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWSS_BASE_URL']
    articles_url = app.config['EVERYTHING_SOURCE_BASE_URL']

def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['results']:
            news_results_list = get_news_response['results']
            news_results = process_results(news_results_list)


    return news_results

    def process_results (news_list):
        '''
        function that processes the news result and transform them to a list of objects
        
        Args:
            news_list: a list of dictionaries that contain news details

        returns:
            news_results: a list of news objects
        '''
        news_results = []
        for news_item in news_list:
            id = news_item.get
            title = news_item.get
            overview = news_item.get
            poster = news_item.get
            vote_average = news_item.get
            vote_count = news_item.get('vote_count')

            if poster:
                news_object = News(id,title,overview,poster,vote_average,vote_count)
                news_results.append(m_object)

        return news_results

def get_articles(news_id, limit):
    '''
    Function that gets articles based on the news id
    '''
    get_article_location_url = articles_url.format(news_id, limit, api_key)

    with urllib.request.urlopen(get_article_location_url) as url:
        articles_location_data = url.read()
        articles_location_response = json.loads(articles_location_data)

        articles_location_results = None

        if articles_location_response['articles']:
            articles_location_results = process_articles(articles_location_response['articles'])

    return articles_location_results


def process_articles(my_articles):
    '''
    Function that processes the json results for the articles
    '''
    article_location_list = []

    for article in my_articles:
        author = article.get('author')
        title = article.get('title')
        description = article.get('description')
        url = article.get('url')
        urlToImage = article.get('urlToImage')

        if urlToImage:
            article_source_object = Articles(author, title, description, url, urlToImage)
            article_location_list.append(article_source_object)

    return article_location_list