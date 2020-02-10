
import urllib.request, json
from .models import Newws, Articles
api_key = None
newws_url = None
base_url = None
articles_url = None
topheadlines_url = None
everything_url = None
everything_search_url = None

#from .models import news
# News = news.News
# # Getting the news base url
# base_url = app.config['https://newsapi.org/v2/top-headlines?'
#        'country=us&']

def configure_request(app):
    global api_key, base_url, articles_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWWS_BASE_URL']
    print('***base news url***')
    print(base_url)

    articles_url = app.config['EVERYTHING_NEWWS_BASE_URL']
    print('***base articles url***')
    print(articles_url)


def get_newws(category):
    '''
    Function that gets the json response to our url request
    '''
    get_newws_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_newws_url) as url:
        get_newws_data = url.read()
        get_newws_response = json.loads(get_newws_data)

        newws_results = None

        if get_newws_response['news']:
            newws_results_list = get_newws_response['newws']
            newws_results = process_news(newws_results_list)


    return newws_results

def process_news (newws_list):
    '''
    function that processes the news result and transform them to a list of objects           
    Args:
    news_list: a list of dictionaries that contain news details
    returns:
    news_results: a list of news objects
    '''
    newws_results = []
    for newws_item in newws_list:
        id = newws_item.get('id')
        name = newws_item.get('name')
        # description = news_item.get('description')
        # url = news_item.get('url')
        # category = news_item.get('category')
        # language = news_item.get('language')
        # country=news_item.get('country')
        # urlToImage=news_item.get('urlToImage')
       # vote_average = news_item.get('category')
        vote_count = newws_item.get('vote_count')

        #if url:
        #news_object = News(id,name,description,url,category,news_results.append(news_object)
        newws_object = Newws(id,name)
        newws_results.append(newws_object)

    return newws_results

def get_articles(newws_id, limit):
    '''
    Function that gets articles based on the news id
    '''
    get_articles_location_url = articles_url.format(newws_id, limit, api_key)

    with urllib.request.urlopen(get_articles_location_url) as url:
        articles_location_data = url.read()
        articles_location_response = json.loads(articles_location_data)

        articles_location_results = None

        if articles_location_response['articles']:
            articles_location_results = process_articles(articles_location_response['articles'])

    return articles_location_results


def process_articles(articles_list):
    '''
    Function that processes the json results for the articles
    '''
    articles_location_list = []

    for article in articles_list:
        id = article.get('id')
        author = article.get('author')
        title = article.get('title')
        description = article.get('description')
        url = article.get('url')
        urlToImage = article.get('urlToImage')

        if urlToImage:
            articles_source_object = Articles(author, title, description, url, urlToImage)
            articles_location_list.append(article_source_object)

    return articles_location_list