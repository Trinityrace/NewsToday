from flask import render_template,request,redirect,url_for
from . import main
from  ..request import get_newws, get_articles
from app.models import Newws
#from  .. import News


# Views
@main.route('/')
def index():
    # get general news

    general_news = get_newws('category')
    business_news = get_newws('business')
    entertainment_news = get_newws('entertainment')
    sports_news = get_newws('sports')
    technology_news = get_newws('technology')
    science_news = get_newws('science')
    health_news = get_newws('health')


    title = 'News Today Site'

    return render_template('index.html', title=title, General=general_news, Business=business_news,
                           Entertainment=entertainment_news, Sports=sports_news, Technology=technology_news,
                           Science=science_news, Health=health_news)
    # # Getting popular news
    # popular_news = get_news('popular')
    # # print(popular_news)
    # upcoming_news = get_news('upcoming')
    # now_showing_news = get_news('now_playing')
    # title = 'Home - Welcome to The best News Review Website Online'
    # return render_template('index.html', title = title, popular = popular_news, upcoming = upcoming_news, now_showing = now_showing_news )

@main.route('/articles/<newws_id>&<int:per_page>')
def articles(newws_id, per_page):
    '''
    Function that returns articles based on their sources
    '''

    news_source = get_articles(newws_id, per_page)
    title = f'{newws_id} | All Articles'
    return render_template('articles.html', title=title, name=newws_id, news= news_source)
