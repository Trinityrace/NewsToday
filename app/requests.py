from app import app
import urllib.request,json
from .models import news


News = news.News

# Getting api key
api_key = app.config['64281a2732dd4fbba93a0ce3e0352cc5']

# Getting the news base url
base_url = app.config['https://newsapi.org/v2/top-headlines?'
       'country=us&']

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