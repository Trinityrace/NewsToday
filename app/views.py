from flask import render_template
from app import app


# Views
@app.route('/')
def index():

    '''
    View root page function returns index page and its data
    '''

    title = 'Home - WELCOME TO BEST NEWS TODAY REVIEW PAGE ONLINE!'
    return render_template('index.html', title = title)
    
    # @app.route('/news/<int:news_id>')  
    # def news(news_id):

    #     '''
    #     View news page function that returns the news details page and its data
    #     '''
    #     return render_template('news.html',id = news_id)
