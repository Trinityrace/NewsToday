from flask import render_template
from . import main
from ..request import get_news, get_articles
from models import News

# Views
@main.route('/')
def index():
    # get general news

    general_news = get_sources('general')
    business_news = get_sources('business')
    entertainment_news = get_sources('entertainment')
    sports_news = get_sources('sports')
    technology_news = get_sources('technology')
    science_news = get_sources('science')
    health_news = get_sources('health')


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

@main.route('/articles/<source_id>&<int:per_page>')
def news(source_id, per_page):
    '''
    Function that returns articles based on their sources
    '''

    news_source = get_articles(source_id, per_page)
    title = f'{source_id} | All Articles'
    return render_template('news.html', title=title, name=source_id, news=news_source)
